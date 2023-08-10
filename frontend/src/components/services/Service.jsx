import { FaTimes } from 'react-icons/fa';

const Service = ({ service, onServiceClick, onDelete}) => {
  return (<div className='option' onDoubleClick={()=>{onServiceClick(service.id)}}>
     <h3>{service.service_name} <FaTimes className='x' onClick= {()=>{onDelete(service.id) }}/></h3>

  </div>);
};

export default Service;
