import { useState } from "react";
const AvgOutput = ({avgOutput}) => {
  const [ patientNo, setPatientNo]= useState([])
  // {setPatientNo([avgOutput.total_patient_no])} 
  // <h2> {!avgOutput.is_digital ? "Not Digital" :"Digital" }</h2>
  return (<div className='option'       >
     <h3>Run: {avgOutput.run_no}</h3>


     <p> Total Patients visited: {avgOutput.total_patient_no} </p>
     <p> Time Taken per patient: {avgOutput.avg_total_time_spent}  mins</p>

     {/* {console.log(patientNo)} */}

  </div>);
};

export default AvgOutput;
