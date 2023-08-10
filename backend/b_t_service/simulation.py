import simpy
import random
from backend.b_t_service.patient import Patient
from backend import db
from backend.models import Output, AvgOutput
# from run import db, QueSimulationRun



class EDQModel():
    # Constructor
    # when simulation model object is build the global variables are passed through the constructor 
    def __init__(self, warm_up_duration,total_duration,
        run_no,patient_interval_time, receptionist_no, receptionist_booking_time, triager_no, nurse_triage_time,
        iot_booking_time,   iot_triage_time, control_delay, is_digital, input_id):

        self.warm_up_duration= warm_up_duration
        self.total_duration =total_duration  
        self.run_no=run_no
        self.patient_interval_time =patient_interval_time
        self.receptionist_no =receptionist_no
        self.receptionist_booking_time =receptionist_booking_time
        self.triager_no =triager_no
        self.nurse_triage_time= nurse_triage_time
        self.iot_booking_time=iot_booking_time
        self.iot_triage_time=iot_triage_time
        self.control_delay = control_delay
        self.is_digital =is_digital
        self.input_id=input_id
  
        self.duration= self.total_duration + self.warm_up_duration
        # simpy variables
        self.env = simpy.Environment()
        # patient variable
        self.patient_tracker = 0
        #List to store output 
        self.list_of_total_time =[]
        self.list_of_patients =[]

       
    #Patients arrival
    def generate_patient_arrivals(self, booker, triager, booking_time, triage_time,digital):
        while True:
            self.patient_tracker += 1
            # creates patient & provide them with id
            patient = Patient(self.patient_tracker)
            # patient attends activities before treatment
            self.env.process(self.booking_and_triaging_service(patient, booker, triager, booking_time, triage_time, digital))
            # Patients arrival to urgent care varies
            # Time until the next patient arrives
            patient_arrival_time = random.uniform((self.patient_interval_time-2),(self.patient_interval_time+2)) 
            # stop the time until the next patient arrives.
            yield self.env.timeout(patient_arrival_time)


    # activity of patient before treatment
    def booking_and_triaging_service(self, patient, booker, triager, booking_time, triage_time, digital):
        # start recording the time
        patient_enter_reception_q_time = self.env.now

        # is receptionist free
        with booker.request() as req:
            # stops the time until nurse is free
            yield req

            # if she is free  patient can go to receptionist and leaves the que
            patient_left_registration_q_time = self.env.now

            # note how much time its taken to get to reception
            time_taken_to_reach_reception = (patient_left_registration_q_time - patient_enter_reception_q_time)

            # If its digital control is placed that takes extra min to book a patient
            if(digital):
                #control delay if it is digital
                patient_registration_time = random.uniform((booking_time-2),(booking_time+2)) 
                + random.uniform((self.control_delay-2),(self.control_delay+2))
            else:
                # no control delay
                patient_registration_time = random.uniform((booking_time-2),(booking_time+2)) 

            # stops the time unitl the next patient is booked
            yield self.env.timeout(patient_registration_time)

        # start recording the waiting time for triage queue
        patient_enter_triage_q_time = self.env.now

        # is triage nurse free
        with triager.request() as req:
            # stops the time until triage nurse is free
            yield req

            # if nurse is free patient go to nurse and leaves the que
            patient_left_triage_q_time = self.env.now
            # note how much time its taken to get to triage nurse
            time_taken_to_reach_nurse = (patient_left_triage_q_time - patient_enter_triage_q_time)
           
            # time that triage nurse takes to triage patient varies
            if(digital):
                #control delay if it is digital
                patient_triage_time = (random.uniform((triage_time-2),(triage_time+2)) 
                + random.uniform((self.control_delay-1),(self.control_delay+1)))
            else:
                # no control delay
                patient_triage_time  = random.uniform((triage_time-2),(triage_time+2)) 

            # stops the time until the next patient is triaged
            yield self.env.timeout(patient_triage_time)
                    
            #time it takes for the patient to reach doctor
            total_time_spent= time_taken_to_reach_nurse + time_taken_to_reach_reception + patient_triage_time + patient_registration_time

            #Add values to tables after warm up
            if self.env.now > self.warm_up_duration:
                #add output
                output = Output(self.run_no, patient.id, time_taken_to_reach_reception, patient_registration_time,
                time_taken_to_reach_nurse, patient_triage_time,total_time_spent, self.is_digital, self.input_id )
                #commit to db
                db.session.add(output)
                db.session.commit()
                #add patient id and their time to the list for avg output
                self.list_of_patients.append(patient.id)
                self.list_of_total_time.append(total_time_spent)
 



    #Transform data into avg output then presist it
    def add_avg_output(self):
        total_patients= len(self.list_of_patients)
        # print(total_patients)
        total =0.0

        for i in range(0, total_patients):
           total = total+ self.list_of_total_time[i]

        avg_total_time_spent = total/total_patients

        avg_output= AvgOutput(self.run_no, total_patients, avg_total_time_spent, self.is_digital, self.input_id)
        db.session.add(avg_output)
        db.session.commit()
       

    # Entry point
    def run(self):
      self.receptionist = simpy.Resource(self.env, capacity=self.receptionist_no)
      self.triage_nurse = simpy.Resource(self.env, capacity= self.triager_no)
      booker = self.receptionist
      triager = self.triage_nurse
        
      if(not self.is_digital):
            booking_time = self.receptionist_booking_time
            triage_time =self.nurse_triage_time
            self.env.process(self.generate_patient_arrivals(booker,triager, booking_time, triage_time, self.is_digital))
            self.env.run( self.duration)
            
      if (self.is_digital):
            booking_time = self.iot_booking_time
            triage_time =self.iot_triage_time
            self.env.process(self.generate_patient_arrivals(booker,triager, booking_time, triage_time, self.is_digital))
            self.env.run( self.duration)




