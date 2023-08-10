import { useState } from "react";

export const AddDepartment = ({onAdd}) => {


    const [department_name, setDepartment_name]= useState('')
    const onSubmit = (e) => {
        // do not want it to submit it to the page
        e.preventDefault()

        if(!department_name) {
            return alert('Please add a department')
           
        }
        //if its text
        onAdd({department_name})
        
         setDepartment_name('')
    }
  return (
      <form className='add-form' onSubmit={onSubmit}>
          <div className='form-control'>
            <label>Department</label>

            <input type='text' placeholder='Add Department' value={department_name} 
            onChange={(e)=> setDepartment_name(e.target.value)}></input>
          
          </div>
            <input type='submit' value='Save Department' className='btn btn-block'></input>
      </form>
  );
};
