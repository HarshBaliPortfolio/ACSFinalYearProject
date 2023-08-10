import { useState } from "react";

export const AddSimulation= ({onAdd}) => {


    const [simulation_name, setSimulation_name]= useState('')
    const onSubmit = (e) => {
        // do not want it to submit it to the page
        e.preventDefault()

        if(!simulation_name) {
            return alert('Please add a Simulation')
           
        }
        //if its text
        onAdd({simulation_name})
        
        setSimulation_name('')
    }
  return (
      <form className='add-form' onSubmit={onSubmit}>
          <div className='form-control'>
            <label>Simulation</label>

            <input type='text' placeholder='Add Simulation' value={simulation_name} 
            onChange={(e)=> setSimulation_name(e.target.value)}></input>
          
          </div>
            <input type='submit' value='Save Simulation' className='btn btn-block'></input>
      </form>
  );
};
