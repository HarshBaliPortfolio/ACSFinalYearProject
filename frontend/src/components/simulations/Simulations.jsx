import Simulation from "./Simulation.jsx";

const Simulations = ({ simulations,  onSimulationClick, onDelete}) => {
   
  return( 
  <>
    {

    simulations.map((simulation)=>(
        <Simulation key= {simulation.id}  simulation= {simulation} onDelete ={onDelete} onSimulationClick={onSimulationClick}/>
        )) }
  </>);
};

export default Simulations;
 