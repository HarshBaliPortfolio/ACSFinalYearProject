
  //fetch departments 
  const fetchDepartments= async ()=>{ 
    const res = await fetch('http://127.0.0.1:5000/departments')
    const data = await res.json()
   return data
  }

  //add departments
  const addDepartment =  async (department)=>{
    console.log(JSON.stringify(department))
    const resp = await fetch(`http://127.0.0.1:5000/department`, {
      'method': 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(department)
    });
    const data = await resp.json();
    
   return data
  }

  // Delete departments
  const deleteDepartment = async(id) =>{
    await fetch(`http://127.0.0.1:5000/department/delete/${id}`, {
        'method': 'DELETE'
      });
  }
  export {fetchDepartments, addDepartment, deleteDepartment}