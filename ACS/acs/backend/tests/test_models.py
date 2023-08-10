from backend.models import Department, Service, Simulation, Input, Output, AvgOutput

def test_new_department():
    #Arrange
    name ="Emergency Department"
    #Assign 
    department = Department(name)
    #Assert
    assert department.department_name == "Emergency Department"

def test_new_service():
    #Arrange
    department_id =1
    name ="BT service"
    #Assign
    service = Service(name, department_id)
    #Assert
    assert service.service_name == "BT service"
    assert service.department_id == 1

def test_new_simulation():
    #Arrange
    service_id =2
    name ="DES for BT Service"
    #Assign
    simulation =Simulation(name, service_id)
    #Assert
    assert simulation.simulation_name == "DES for BT Service"
    assert simulation.service_id == 2

def test_new_input():
    #Arrange 
    warm_up= 100
    total_duration =1440
    total_runs_no =10
    patient_interval_time =5
    receptionist_no =1
    receptionist_booking_time =5
    triager_no=1
    nurse_triage_time =10
    iot_booking_time =4
    iot_triage_time =6
    control_delay=1
    simulation_id=1
    #Assign
    input = Input(warm_up,total_duration,total_runs_no, 
    patient_interval_time,receptionist_no, receptionist_booking_time, 
    triager_no, nurse_triage_time,
    iot_booking_time, iot_triage_time, control_delay, simulation_id)
    #Assert 
    assert input.warm_up_duration == warm_up
    assert input.total_duration == total_duration
    assert input.total_runs_no == total_runs_no
    assert input.patient_interval_time == patient_interval_time
    assert input.receptionist_no == receptionist_no
    assert input.receptionist_booking_time == receptionist_booking_time
    assert input.triager_no == triager_no
    assert input.nurse_triage_time == nurse_triage_time
    assert input.iot_booking_time == iot_booking_time
    assert input.iot_triage_time == iot_triage_time
    assert input.control_delay == control_delay
    assert input.simulation_id == simulation_id


def test_new_output():
   #Arrange
   run_no=10    
   patient_no= 1    
   time_spent_in_booking_q= 5
   time_spent_while_booking= 5
   time_spent_in_triage_q= 10
   time_spent_while_triaging=12
   total_time_spent=32
   is_digital = True
   input_id =2
   #Assign 
   output = Output(run_no,patient_no,time_spent_in_booking_q,  
   time_spent_while_booking,time_spent_in_triage_q, 
   time_spent_while_triaging,total_time_spent, is_digital, input_id)
   #Assert
   assert output.run_no ==run_no
   assert output.patient_no ==patient_no
   assert output.time_spent_in_booking_q ==time_spent_in_booking_q
   assert output.time_spent_while_booking ==time_spent_while_booking
   assert output.time_spent_in_triage_q ==time_spent_in_triage_q
   assert output.time_spent_while_triaging ==time_spent_while_triaging
   assert output.total_time_spent ==total_time_spent
   assert output.is_digital == True
   assert output.input_id ==input_id



def test_new_avgoutput():
   #Arrange
   run_no=1   
   total_patient_no= 100
   avg_total_time_spent= 5
   is_digital = True
   input_id =2
   #Assign
   avg_output =AvgOutput(run_no, total_patient_no, avg_total_time_spent, is_digital, input_id)
   #Assert
   assert avg_output.run_no ==run_no
   assert avg_output.total_patient_no ==total_patient_no
   assert avg_total_time_spent == avg_total_time_spent
   assert is_digital == is_digital
   assert input_id == input_id