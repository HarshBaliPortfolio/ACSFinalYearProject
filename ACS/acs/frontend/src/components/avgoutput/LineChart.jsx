import {Line} from "react-chartjs-3";





const LineChart = ({digitalisedData, normalData, runs}) => {
 
  return (<>
  <Line
    data =
    {
      {
        labels: runs,
        datasets : 
        [
           {
             label: "Digitalised service",
             data: digitalisedData,
             backgroundColor: 'rgb(75, 192, 192)',
           },
           {
            label: "Normal service",
            data: normalData,
            backgroundColor: 'rgb(255,255,0)',
          }
        ]   
      }
    }
    height ={300}
    width ={600}
    
    options={
      {
        maintainAspectRatio: true
    
    }
    
  
  } 
    />
    
    
    
    
    </>
  );
}

export default LineChart