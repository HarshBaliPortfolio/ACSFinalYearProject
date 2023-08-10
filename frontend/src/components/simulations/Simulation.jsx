import { FaTimes } from 'react-icons/fa';

const Simulation = ({simulation, onSimulationClick, onDelete} ) => {
  return (<div className='option' onDoubleClick={()=>{onSimulationClick(simulation.id)}}>
     <h3>{simulation.simulation_name} <FaTimes className='x' onClick= {()=>{onDelete(simulation.id) }}/></h3>

  </div>
  );
}

export default Simulation