import Service from "./Service";

const Services = ({ services,  onServiceClick, onDelete}) => {
   
  return( 
  <>
    {

       services.map((service)=>(
        <Service key= {service.id}  service= {service} onDelete ={onDelete} onServiceClick={onServiceClick}/>
        )) }
  </>);
};

export default Services;
 