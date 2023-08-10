import './App.css';
import Header from './components/Header';
import { useState, useEffect } from "react";
import Services from './components/services/Services';
import Departments from './components/departments/Departments';
import { AddDepartment } from './components/departments/AddDepartment';
import { AddService } from './components/services/AddService';
import Simulations from './components/simulations/Simulations';
import { AddSimulation } from './components/simulations/AddSimulation';
import { Input } from './components/input/Input';
import{fetchDepartments, addDepartment, deleteDepartment} from './components/departments/ApiDepartments';
import { fetchServices, deleteService, addService } from './components/services/ApiService';
import { fetchSimulations, deleteSimulation, addSimulation} from './components/simulations/ApiSimulation';
import { Btn } from './components/Btn';
import { addInput, fetchInputs } from './components/input/ApiInput';
import {fetchAvgOutput} from './components/avgoutput/ApiAvgOutput';
import AvgOutputs from './components/avgoutput/AvgOutputs';
import PreviousInputs from './components/input/PreviousInputs';
import Statistics from './components/statistics/Statistics';
import BarChart from './components/avgoutput/BarChart';
import PieChart from './components/avgoutput/PieChart';
import LineChart from './components/avgoutput/LineChart';





function App() {

//TODO: the forms should have same use state variables as the models in flask
// todo : link simulation with service click 
  
   const [departments, setDepartments]= useState([])
   const [services, setServices]= useState([])
   const [simulations, setSimulations]= useState([])
   const [input, setInput]= useState([])
   const [inputs, setInputs]= useState([])
   const [avgOutputs, setAvgOutputs]= useState([])

  //  use it when to fetch the results

  // use to render the add form
   const [showAdd, setShowAdd]= useState(false)

   //informs react to render the state according to system state
   const[state, setState] = useState('')


   // require to store foreign key id  [vital for navigation ]
   const [backref, setBackref]= useState()

   const [simuref, setSimuref]= useState()

   
   const [simulationName , setSimulationName ]= useState('')

    var userInputId

  //use to render +/- form button dynamically
   const inputButton =true

   const [digitalisedData, setDigitalisedData ] = useState([])

   const [normalData, setNormalData] =useState([])
   const [digitalPatients, setDigitalPatients] =useState([])
   const [normPatients, setNormPatients] =useState([])

   const [runs, setRuns]= useState([])

   const [longestDigitalRunNo, setLongestDigitalRunNo]= useState()
   const [longestDigitalTime, setLongestDigitalTime]= useState()
   const [longestDigitalPatient, setLongestDigitalPatient]= useState()
   const [longestDigitalDailyVisits, setLongestDigitalDailyVisits]= useState()   

   const [shortestDigitalTime, setShortestDigitalTime]= useState()
   const [shortestDigitalRunNo, setShortestDigitalRunNo]= useState()
   const [shortestDigitalPatient, setShortestDigitalPatient]= useState()
   const [shortestDigitalDailyVisits, setShortestDigitalDailyVisits]= useState()   

   const [shortestTime, setShortestTime]= useState()
   const [shortestRunNo, setShortestRunNo]= useState()
   const [shortestPatient, setShortestPatient]= useState()
   const [shortestDailyVisits, setShortestDailyVisits]= useState()   

   const [longestTime, setLongestTime]= useState()
   const [longestPatient, setLongestPatient]= useState()
   const [longestRunNo, setLongestRunNo]= useState()
   const [longestDailyVisits, setLongestDailyVisits]= useState() 




useEffect(()=>{
  getDepartments()
  setState('Show Departments')
}, 
[])

                               //DEPARTMENTS
// Makes get api call and fetches data  and store it in departments
const getDepartments = async () =>{
   const dept = await fetchDepartments()
    setDepartments(dept)
  }
//Makes Post api call and adds departmentds 
const activateAddDepartment = async (department) =>{
  const data = await addDepartment(department)
  setDepartments([...departments, data])
}
//Wen departments r double clicked get the services
const onDepartmentClick= (id)=>{
     setBackref(id)
     getServices(id)
  }
// Make DELETE api call and delete department 
const activateDeleteDepartment = async (id)=>{
 const deleteVal= window.confirm("Do you want to delete this department?")
 if(deleteVal){
  await deleteDepartment(id)
  setDepartments(departments.filter((department)=> department.id !==id))
 }
}

                                    //SERVICES
// Makes get api call and fetches data  and store it in usestate
const getServices = async(id)=>{
  const services = await fetchServices(id)
  setServices(services)
  setState('Show Services')
}
//wen services are double clicked get the simulations
const onServiceClick= async(id)=>{
    setBackref(id)
    getSimulations(id)
  }
// delete Servics
const activateDeleteService = async (id)=>{
  const deleteVal= window.confirm("Do you want to delete?")
  if(deleteVal){
   await deleteService(id)
   setServices(services.filter((service)=> service.id !==id))
  }
  }
//add Service
const activateAddService =  async (service)=>{
   const data = await addService(backref, service)
   setServices([...services, data])
  }




                                        //Simulations
//GET
const getSimulations= async(id)=>{
    const simulations = await fetchSimulations(id)
    setSimulations(simulations)
    setState('Show Simulations')
    setBackref(id)// back ref for service
  }
//CLICK
const onSimulationClick= async(id)=>{
     setSimuref(id)
     setState('decision')
}
//DELETE
const activateDeleteSimulation = async (id)=>{
  const deleteVal= window.confirm("Do you want to delete?") 
  if(deleteVal){
   await deleteSimulation(id)
   setSimulations(simulations.filter((simulation)=> simulation.id !==id))
  }
  }
  //add Service
const activateAddSimulation =  async (simulation)=>{
    const data = await addSimulation(backref, simulation)
    setSimulations(data)
  }






                              // INPUT
  // On run add input  
  const onRun = async()=>{
    setState('Add Input')
   }

   //fetches the avgoutput from db through backend
  const startSimulating= async(inputData)=>{
    const data = await addInput(simuref, inputData) //get  data, that is stored in db after posting
    setInput(data) // set the input to data 
    console.log(input)
    userInputId =data.id // get the input id 
    console.log(userInputId)
    getAvgOutput(userInputId)
  }

  const onView = async()=>{
     const data = await fetchInputs(simuref)
     setInputs(data)
     setState('view')
     
  }


                          //OUTPUT
  const getAvgOutput= async(userInputId)=>{
    const avgOutput = await fetchAvgOutput(userInputId)// fetch the avg output data tht has user input id
    setAvgOutputs(avgOutput)
    //  activateFillChartData()
    setState('Show Output')  
  }

  const onInputClick = async(id)=>{
    const avgOutput = await fetchAvgOutput(id)// fetch the avg output data tht has user input id
    setAvgOutputs(avgOutput)
    
    setState('Show Output')    
    
    
  }


                      //chart 


  const fillChartData = ()=>{
   const data =   avgOutputs.filter((avgOutput) =>(avgOutput.is_digital)).map((avgOutput)=>(avgOutput.avg_total_time_spent))
   const patients = avgOutputs.filter((avgOutput) =>(avgOutput.is_digital)).map((avgOutput)=>(avgOutput.total_patient_no))
   const normData = avgOutputs.filter((avgOutput) =>(!avgOutput.is_digital)).map((avgOutput)=>(avgOutput.avg_total_time_spent))
   const normPatients =  avgOutputs.filter((avgOutput) =>(!avgOutput.is_digital)).map((avgOutput)=>(avgOutput.total_patient_no))
   const runData = avgOutputs.filter((avgOutput) =>(avgOutput.is_digital)).map((avgOutput)=>(avgOutput.run_no))
   console.log(patients)
   console.log(normPatients)
   setDigitalPatients(patients)
   setNormPatients(normPatients)
   setDigitalisedData(data)
   setNormalData(normData)
   setRuns(runData)

  longestDTime(data, patients)
  shortestDTime(data, patients)
  longestHTime(normData,normPatients)
  shortestHTime(normData,normPatients)
   setState('Show Statistics')

  }
  

  const workoutDailyVisits =(patient,time )=>{
   const visits =(patient / time) * 1440
    return Math.ceil( visits)
  }


  // longest shortest
  const longestDTime=(data,patients)=>{
    let longestDigitalTime =data[0]
    let patient 
    let i 
    for ( i=0; i < data.length; i++) {
      if (data[i]>=longestDigitalTime){
        longestDigitalTime=data[i]
        patient = patients[i]
        setLongestDigitalRunNo(i)

      }

    }
    setLongestDigitalDailyVisits(workoutDailyVisits(patient, longestDigitalTime))
    setLongestDigitalPatient(patient)
    setLongestDigitalTime(longestDigitalTime)
  }
  

    // longest shortest
  const shortestDTime=(data,patients)=>{
      let shortestDigitalTime =data[0]
      let patient 
      let i 
      for ( i=0; i < data.length; i++) {
        if (data[i]<=shortestDigitalTime){
          shortestDigitalTime=data[i]
          patient = patients[i]
          setShortestDigitalRunNo(i)
        }
  
      }

      setShortestDigitalDailyVisits(workoutDailyVisits(patient, shortestDigitalTime))
      setShortestDigitalPatient(patient)
      setShortestDigitalTime(shortestDigitalTime)
  }

    // longest shortest
  const longestHTime=(normData,norPatients)=>{
      let longestTime =normData[0]
      let patient 
      let i 
      for ( i=0; i < normData.length; i++) {
        if (normData[i]>=longestTime){
          longestTime=normData[i]
          patient = norPatients[i]
          setLongestRunNo(i)
        }
      }
     setLongestDailyVisits(workoutDailyVisits(patient, longestTime))
     setLongestPatient(patient)
     setLongestTime(longestTime)
    }
  
        // longest shortest
  const shortestHTime=(normData,norPatients)=>{
    let shortestTime =normData[0]
    let patient
    let i 
    for ( i=0; i < normData.length; i++) {
      if (normData[i]<=shortestTime){
        shortestTime=normData[i]
        patient = norPatients[i]
      }
      setShortestRunNo(i)
    }
    setShortestDailyVisits(workoutDailyVisits(patient, shortestTime))
    workoutDailyVisits(patient, shortestTime)
    setShortestPatient(patient)
    setShortestTime(shortestTime)
  }


  const startVisualising=()=>{
    setState('Visualise Statistics')
  }

                                  //HOME ICON
  //when home icon is clicked load back to departments                                          
  const goHome = ()=>{
    getDepartments()
    setState('Show Departments')
  }

  const goServices = ()=>{
    getServices(backref)
    setState('Show Services')
  }

  const goSimulations = ()=>{
    getSimulations(backref)
    setState('Show Simulations')
  }
             
// condition for output to dynamically load components
let output
switch (state) {
  // initial state
  case 'Show Departments': 
    output= <div className="container">

      {/* header component */}
      <Header  title= 'Departments'  onAdd={()=> setShowAdd(!showAdd)}
      buttonVal={showAdd} inputButton ={inputButton}/>
      {/* add button component*/}
      {showAdd && <AddDepartment onAdd ={activateAddDepartment} />}

      {/* show departments using departments component */}
      <Departments departments ={departments} onDelete={activateDeleteDepartment}
       onDepartmentClick={onDepartmentClick} />
    </div>
    break;
  
  case 'Show Services' :
    output= <div
    className="container">  
      {/* header component */}
      <Header  title= 'Services' home ={goHome} onBackClick={goHome} 
      onAdd={()=> setShowAdd(!showAdd)} 
      inputButton ={inputButton} buttonVal={showAdd} />
        {/* add simulation component*/}
      {showAdd && <AddService onAdd ={activateAddService} />}
        {/* show services using services component */}
      <Services services ={services} onDelete={activateDeleteService} 
      onServiceClick ={onServiceClick}/>
  </div>
  break;

  case 'Show Simulations':
    output= <div
    className="container">  
     {/* header component */}
      <Header  title= 'Simulations' home ={goHome} onBackClick={goServices} inputButton ={inputButton} 
      onAdd={()=> setShowAdd(!showAdd)} buttonVal={showAdd} />
        {/* add simulation component*/}
      {showAdd && <AddSimulation onAdd ={activateAddSimulation} />}
          {/* show simulations using simulations component */}
      <Simulations simulations ={simulations} onDelete={activateDeleteSimulation} 
      onSimulationClick ={onSimulationClick} />
  </div>
  break;

  case 'decision':
     {/* header component */}
    output =<div className='container'>
    <Header  title= 'Choose' home ={goHome} onBackClick={goSimulations} 
    inputButton ={!inputButton}
    // do not show add button
    onAdd={()=> setShowAdd(!showAdd)} buttonVal={showAdd} />
    {/* View btn component */}
    <br></br>
    <Btn text='View' color = 'blue' onClick={onView}/>
     {/* Run btn component */}
    <br></br>
    <Btn text='Run' color = 'green' onClick={onRun}/>
    </div>
    break;

  case 'Add Input':
    output = <div className='container'>
       {/* header component */}
    <Header  title= 'Inputs' home ={goHome} onBackClick={goSimulations} inputButton ={!inputButton}
    onAdd={()=> setShowAdd(!showAdd)} buttonVal={showAdd} />
     {/* input component */}
    <Input onAdd={startSimulating} />
  </div>
    break;


  case 'view':
      output = <div className='container'>
      <Header  title= 'Previous Simulations' home ={goHome} onBackClick={goSimulations} inputButton ={!inputButton}
      onAdd={()=> setShowAdd(!showAdd)} buttonVal={showAdd} />
      <PreviousInputs inputs ={inputs} onInputClick ={onInputClick} onSimuClick ={(name)=> setSimulationName(name)}/>
    </div>
     break;

     //container has 2 container  OUTPUT & DIGITAL OUTPUT
  case 'Show Output':
      output = <div className='container'>
        <Header  title= {simulationName} home ={goHome} onBackClick={goSimulations} inputButton ={!inputButton} 
          onAdd={()=> setShowAdd(!showAdd)} buttonVal={showAdd} />          
          <AvgOutputs avgOutputs={avgOutputs} />  
       
         <Btn text={'Statistics'} color={'steelblue'} onClick={fillChartData}/>
      </div>
    break;

    case 'Show Statistics':
      output = <div className='container'>
      <Header  title= 'Statistics' home ={goHome} onBackClick={goSimulations} inputButton ={!inputButton}
      onAdd={()=> setShowAdd(!showAdd)} buttonVal={showAdd} />
        <Statistics title ={'As Is'} longestTime ={longestTime}  shortestTime={shortestTime} lRun ={longestRunNo} 
        sRun ={shortestRunNo} lPatient ={longestPatient} sPateint={shortestPatient}
        lDVisits ={longestDailyVisits} sDVisits ={shortestDailyVisits}/>

        <Statistics title ={'Digital'} longestTime ={longestDigitalTime}  shortestTime={shortestDigitalTime} lRun ={longestDigitalRunNo} 
        sRun ={shortestDigitalRunNo} lPatient ={longestDigitalPatient} sPateint={shortestDigitalPatient} dailyVisits 
        lDVisits ={longestDigitalDailyVisits} sDVisits ={shortestDigitalDailyVisits}/>

      <Btn text={'Visualise'} color={'steelblue'} onClick={startVisualising}/>
      </div>
    break;

  case 'Visualise Statistics':
    output = <div>
       <Header  title= 'Output' home ={goHome} onBackClick={goSimulations} inputButton ={!inputButton} 
          onAdd={()=> setShowAdd(!showAdd)} buttonVal={showAdd} />
      <div className='flex-container'> 
     
      <div className='flex-child'>
        <h1 style={{textAlign: "center"}}>Comparing Daily Patient visits</h1>
             <PieChart   lDVisits ={longestDailyVisits} sDVisits ={shortestDailyVisits} dLDVisits ={longestDigitalDailyVisits} 
             dSDVisits ={shortestDigitalDailyVisits}/>
          </div>

          <div className='flex-child'>
        <h1 style={{textAlign: "center"}}>Time Spent per Run </h1>
        <BarChart digitalisedData ={digitalisedData} normalData ={normalData} runs={runs} yAxis={'Time (Minutes)'}/> 
          </div>
          </div>

      <div className='flex-container'> 
      <div className='flex-child'>
        <h1 style={{textAlign: "center"}}> Patient Visits Per Run</h1>
             <BarChart digitalisedData ={digitalPatients} normalData ={normPatients} runs={runs} yAxis={'Patient No.'}/>
          </div>
          </div>

       
          </div>
    break;

}

//return this in the root in index.html
return (<>{output}</>
    
  );
}

export default App;
