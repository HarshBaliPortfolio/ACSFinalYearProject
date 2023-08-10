import Department from "./Department";

const Departments = ({ departments,  onDelete, onDepartmentClick}) => {
   
  return( 
  <>
    {
       departments.map((department)=>(
        <Department key= {department.id}  onDelete ={onDelete} department= {department} onDepartmentClick={onDepartmentClick}/>
        )) }
  </>);
};

export default Departments;
 