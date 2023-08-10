// fetch services 
const fetchServices= async(id)=>{
    const res = await fetch(`http://127.0.0.1:5000/department/${id}/services`)
    const data = await res.json()
   return data
  }

const deleteService = async(id) => {
    await fetch(`http://127.0.0.1:5000/department/service/delete/${id}`, {
    'method': 'DELETE'
    });
}

// add service
const addService = async(backref, service) =>{
    const resp = await fetch(`http://127.0.0.1:5000/department/${backref}/service`, {
      'method': 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(service)
    });
    const data = await resp.json();
    return data
}

  export {fetchServices, deleteService, addService}