const fetchSimulations= async(id)=>{
    const res = await fetch(`http://127.0.0.1:5000/service/${id}/simulations`)
    const data = await res.json()
  return data
}

const deleteSimulation = async(id) => {
 await fetch(`http://127.0.0.1:5000/service/simulation/delete/${id}/`, {
    'method': 'DELETE'
    });
}


// Add Simulation
const addSimulation = async(serviceId, simulation) =>{
  const resp = await fetch(`http://127.0.0.1:5000/service/${serviceId}/simulation`, {
    'method': 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(simulation)
  });
  const data = await resp.json();
  return data
}



export {fetchSimulations, deleteSimulation, addSimulation}