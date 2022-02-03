import simpy
import random
from patient import Patient
from models import db, QueSimulationRun








class EDQModel():
    # Constructor
    def __init__(self, warm_up_duration,total_duration,
        run_no,patient_interval_time, receptionist_no, receptionist_booking_time, triage_nurse_no, nurse_triage_time,
        booking_iot_no, iot_booking_time, triage_iot_no,  iot_triage_time, simulation_id):

        self.warm_up_duration= warm_up_duration
        self.total_duration =total_duration  
        self.run_no=run_no
        self.patient_interval_time =patient_interval_time
        self.receptionist_no =receptionist_no
        self.receptionist_booking_time =receptionist_booking_time
        self.triage_nurse_no =triage_nurse_no
        self.nurse_triage_time= nurse_triage_time
        self.booking_iot_no=booking_iot_no
        self.iot_booking_time=iot_booking_time
        self.triage_iot_no=triage_iot_no
        self.iot_triage_time=iot_triage_time
        self.simulation_id=simulation_id
        
        print(self.patient_interval_time)


        self.env = simpy.Environment()
        self.patient_tracker = 0

 

    def generate_patient_arrivals(self, booker, triager, booking_time, triage_time):
        while True:
            self.patient_tracker += 1

            # creates patient & provide them with id
            patient = Patient(self.patient_tracker)

            # patient attends activities before treatment
            self.env.process(self.pretreatment_activity(patient, booker, triager, booking_time, triage_time))

            # Patients arrival to urgent care varies
            # Time until the next patient arrives
            patient_arrival_time = random.expovariate(1.0 / self.patient_interval_time)

            # stop the time until the next patient arrives.
            yield self.env.timeout(patient_arrival_time)

    def pretreatment_activity(self, patient, booker, triager, booking_time, triage_time):
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
            print('patientname: ', patient.id, ' time taken to reach reception= ', time_taken_to_reach_reception)

            # time that recptionist takes to register patient varies
            patient_registration_time = random.expovariate(1.0 / booking_time)

            # stops the time unitl the next patient is booked
            yield self.env.timeout(patient_registration_time)

        # start recording the time
        patient_enter_triage_q_time = self.env.now

        # is triage nurse free
        with triager.request() as req:
            # stops the time until triage nurse is free
            yield req

            # if nurse is free patient go to nurse and leaves the que
            patient_left_triage_q_time = self.env.now

            # note how much time its taken to get to triage nurse
            time_taken_to_reach_nurse = (patient_left_triage_q_time - patient_enter_triage_q_time)
            print('patientname: ', patient.id, ' time taken to reach triage= ', time_taken_to_reach_nurse)
            # time that triage nurse takes to triage patient varies
            patient_triage_time = random.expovariate(1.0 / triage_time)

            # stops the time until the next patient is triaged
            yield self.env.timeout(patient_triage_time)
            print('patientname: ', patient.id, ' total time in que= ', (time_taken_to_reach_nurse + time_taken_to_reach_reception + patient_triage_time + patient_registration_time))

            total_time_spent= time_taken_to_reach_nurse + time_taken_to_reach_reception + patient_triage_time + patient_registration_time

            que_simulation_run = QueSimulationRun(self.run_no, patient.id, time_taken_to_reach_reception, patient_registration_time,
            time_taken_to_reach_nurse, patient_triage_time,total_time_spent,self.simulation_id )
            db.session.add(que_simulation_run)
            db.session.commit()








    def run(self):
        duration= self.total_duration
        if((self.booking_iot_no == 0) or (self.triage_iot_no==0)):
            self.receptionist = simpy.Resource(self.env, capacity=self.receptionist_no)
            self.triage_nurse = simpy.Resource(self.env, capacity= self.triage_nurse_no)

            booker = self.receptionist
            booking_time = self.receptionist_booking_time
            triager = self.triage_nurse
            triage_time =self.nurse_triage_time

            self.env.process(self.generate_patient_arrivals(booker,triager, booking_time, triage_time))
            self.env.run(until = duration)
        else:
            self.booking_iot =simpy.Resource(self.env, capacity= self.booking_iot_no)

            self.triage_iot = simpy.Resource(self.env, capacity= self.triage_iot_no)
            booker = self.booking_iot
            booking_time = self.iot_booking_time
            triager = self.triage_iot
            triage_time =self.iot_triage_time

            self.env.process(self.generate_patient_arrivals(booker,triager, booking_time, triage_time))
            self.env.run(until = duration)




