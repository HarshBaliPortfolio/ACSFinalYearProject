import { useState } from "react";

export const AddService = ({onAdd}) => {


    const [service_name, setService_name]= useState('')
    const onSubmit = (e) => {
        // do not want it to submit it to the page
        e.preventDefault()

        if(!service_name) {
            return alert('Please add a Service')
           
        }
        //if its text
        onAdd({service_name})
        
         setService_name('')
    }
  return (
      <form className='add-form' onSubmit={onSubmit}>
          <div className='form-control'>
            <label>Service</label>

            <input type='text' placeholder='Add Service' value={service_name} 
            onChange={(e)=> setService_name(e.target.value)}></input>
          
          </div>
            <input type='submit' value='Save Service' className='btn btn-block'></input>
      </form>
  );
};
