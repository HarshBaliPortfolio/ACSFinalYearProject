
// add Input
const addInput= async(simuref, inputData)=>{
 const resp = await fetch(`http://127.0.0.1:5000/simulation/${simuref}/input`,
  {
    'method': 'POST',
    headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(inputData)
   }
 );
      const data = await resp.json();
    return data
     
}


const fetchInputs =async(id)=>{
  const res = await fetch(`http://127.0.0.1:5000/simulation/${id}/inputs`)
  const data = await res.json()
 return data
}

export {addInput, fetchInputs}