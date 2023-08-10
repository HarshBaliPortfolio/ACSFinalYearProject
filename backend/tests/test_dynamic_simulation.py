
import backend.b_t_service.simulation as simulation

def test_dynamic_as_is():
    #Arrange
    warm_up= 100
    total_duration =200
    run_no =1
    patient_interval_time =5
    receptionist_no =1
    receptionist_booking_time =5
    triager_no=1
    nurse_triage_time =10
    iot_booking_time =4
    iot_triage_time =6
    control_delay =2
    is_digital= False
    input_id =1
    #Assign
    sim =simulation.EDQModel(warm_up,total_duration,run_no,
    patient_interval_time,receptionist_no, receptionist_booking_time,
     triager_no, nurse_triage_time,
    iot_booking_time,  iot_triage_time,control_delay, is_digital,input_id)
    sim.run()
    #Assert
    #time spent in booking and triaging service by patient with id 1 
    #should be more than booking time + triage time
    assert sim.list_of_total_time[1] > receptionist_booking_time+ nurse_triage_time

def test_dynamic_digital():
    #Arrange
    warm_up= 100
    total_duration =200
    run_no =1
    patient_interval_time =5
    receptionist_no =1
    receptionist_booking_time =5
    triager_no=1
    nurse_triage_time =10
    iot_booking_time =4
    iot_triage_time =6
    control_delay =2
    is_digital= True
    input_id =1
    #Assign
    sim =simulation.EDQModel(warm_up,total_duration,run_no,
    patient_interval_time,receptionist_no, receptionist_booking_time, triager_no,
     nurse_triage_time,
    iot_booking_time,  iot_triage_time,control_delay, is_digital,input_id)
    sim.run()
    #Assert
    #time spent in booking and triaging service by patient with id 1 
    #should be more than booking time + triage time
    assert sim.list_of_total_time[1] > receptionist_booking_time+ nurse_triage_time


