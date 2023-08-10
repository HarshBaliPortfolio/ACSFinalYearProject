import React from 'react'

const Statistics = ({title, longestTime, shortestTime, lRun, sRun, lPatient, sPateint, lDVisits, sDVisits}) => {
  return (
    <div className='option'>
         <h1>{title}</h1>
        <div className='results'>
            <h3>Longest time :{longestTime}</h3>
            <p>Patients visited: {lPatient} </p>
            <p>Run no: {lRun}</p>
         
              <p>Per Day visits: {lDVisits} </p>
          
        </div>
        <div className='results'>
            <h3>Shortest time :{shortestTime}</h3>
            <p>Patients visited: {sPateint} </p>
            <p>Run no: {sRun}</p>
            
              <p>Per Day visits:{sDVisits}</p>
           
        </div>
  </div>

  )
}

export default Statistics