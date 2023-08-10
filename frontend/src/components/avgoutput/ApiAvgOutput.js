const fetchAvgOutput= async(id)=>{
    const res = await fetch(`http://127.0.0.1:5000/input/${id}/avg/outputs`)
    const data = await res.json()
   return data
  }

export{fetchAvgOutput}