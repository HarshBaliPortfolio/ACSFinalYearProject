import { FaTimes } from 'react-icons/fa';

const Department = ({department, onDepartmentClick, onDelete}) => {
  return (<div className='option' onDoubleClick={()=>{onDepartmentClick(department.id)}}  >
     <h3>{department.department_name} <FaTimes className='x' onClick= {()=>{onDelete(department.id)}}/></h3>

  </div>);
};

export default Department;
