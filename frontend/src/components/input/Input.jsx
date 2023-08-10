import { useState } from "react";

export const Input = ({onAdd}) => {


    const [ warm_up_duration, setWarm_up_duration]= useState()
    const[total_runs_no, setTotal_runs_no] = useState()
    const [ total_duration, setTotal_duration]= useState()
    const [ patient_interval_time, setPatient_interval_time]= useState()
    const [ receptionist_no, setReceptionist_no]= useState()
    const [ receptionist_booking_time, setReceptionist_booking_time]= useState()
    const [ triager_no, setTriager_no]= useState()
    const [ nurse_triage_time, setNurse_triage_time]= useState()
    const [ iot_triage_time, setIot_triage_time]= useState()
    const [ iot_booking_time, setIot_booking_time]= useState()
    const [ control_delay,setControl_delay ]= useState()

    const onSubmit = (e) => {
        // do not want it to submit it to the page
        e.preventDefault()

        //verifications
        if((!warm_up_duration)||(!total_duration) ||(!total_runs_no)||(!patient_interval_time) ||
        (!receptionist_no)|| (!receptionist_booking_time)|| (!triager_no)|| (!nurse_triage_time) 
        ||(!iot_booking_time) || (!iot_triage_time)|| (!control_delay)) 
        {
          return alert('Input fields missing')
        }
        if(warm_up_duration<100){
          return alert('Warm up duration should be more than 100')
        }
        if(total_duration < 0){
          return alert('Collection time cannot be less than 0')
        }

        if(iot_booking_time >= receptionist_booking_time){
          return alert('IoT device should take less time to book than receptionist')
        }

        if(iot_triage_time >= nurse_triage_time){
          return alert('IoT device should take less time triage than nurse')

        }
        if(control_delay>= iot_booking_time ){
        return alert('Delay should be less than IoT speed to book')
        }
        //if its text
        onAdd({warm_up_duration, total_duration, total_runs_no,
          patient_interval_time, receptionist_no, receptionist_booking_time,triager_no,
           nurse_triage_time, iot_booking_time, iot_triage_time, control_delay})
        
        setWarm_up_duration()
        setTotal_duration()
        setTotal_runs_no()
        setNurse_triage_time()
        setReceptionist_no()
        setReceptionist_booking_time()
        setTriager_no()
        setNurse_triage_time()
        setIot_triage_time()
        setIot_booking_time()
        setControl_delay()

    }
  return (
      <form className='add-form' onSubmit={onSubmit}>

          <div className='form-control'>
            <label>Warm-up Duration (mins)</label>
            <input type='number' placeholder='e.g. 60' value={warm_up_duration} 
            onChange={(e)=> setWarm_up_duration(e.target.valueAsNumber)}></input>
          </div>
          <div className='form-control'>
            <label>Collection Duration (mins)</label>
            <input type='number' placeholder='e.g. 120' value={total_duration} 
            onChange={(e)=> setTotal_duration(e.target.valueAsNumber)}></input>
          </div>

          <div className='form-control'>
            <label>Total Runs</label>
            <input type='number' placeholder='e.g. 100' value={total_runs_no} 
            onChange={(e)=> setTotal_runs_no(e.target.valueAsNumber)}></input>
          </div>
          <div className='form-control'>
            <label>Patient Interval Time (mins)</label>
            <input type='number' placeholder='e.g. 5' value={patient_interval_time} 
            onChange={(e)=> setPatient_interval_time(e.target.valueAsNumber)}></input>
          </div>
          <div className='form-control'>
            <label>Receptionist No.</label>
            <input type='number' placeholder='e.g. 1' value={receptionist_no} 
            onChange={(e)=> setReceptionist_no(e.target.valueAsNumber)}></input>
          </div>
          <div className='form-control'>
            <label>Receptionist Booking Time (mins)</label>
            <input type='number' placeholder='e.g. 5' value={receptionist_booking_time} 
            onChange={(e)=> setReceptionist_booking_time(e.target.valueAsNumber)}></input>
          </div>
          <div className='form-control'>
            <label>Triage Nurse No.</label>
            <input type='number' placeholder='e.g. 2' value={triager_no} 
            onChange={(e)=> setTriager_no(e.target.valueAsNumber)}></input>
          </div>
          <div className='form-control'>
            <label>Triage Time (mins)</label>
            <input type='number' placeholder='e.g. 10' value={nurse_triage_time} 
            onChange={(e)=> setNurse_triage_time(e.target.valueAsNumber)}></input>
          </div>

          <div className='form-control'>
            <label>Time IOT takes to book: (mins)</label>
            <input type='number' placeholder='e.g. 3' value={iot_booking_time} 
            onChange={(e)=> setIot_booking_time(e.target.valueAsNumber)}></input>
          </div>
          <div className='form-control'>
            <label>Time IOT takes to Triage: (mins)</label>
            <input type='number' placeholder='e.g. 5' value={iot_triage_time} 
            onChange={(e)=> setIot_triage_time(e.target.valueAsNumber)}></input>
          </div>
          <div className='form-control'>
            <label>Delay due to Security Control: (mins)</label>
            <input type='number' placeholder='e.g. 5' value={control_delay} 
            onChange={(e)=> setControl_delay(e.target.valueAsNumber)}></input>
          </div>


            <input type='submit' value='Start' className='btn btn-block'></input>
      </form>
  );
};
