import { Bar } from "react-chartjs-3";





const LineChart = ({digitalisedData, normalData, runs,  yAxis}) => {
 
  return (<>
  <Bar
    data =
    {
      {
        labels: runs,
        datasets : 
        [
           {
             label: "Digitalised service",
             data: digitalisedData,
             backgroundColor: 'rgb(255, 99, 132)',
           },
           {
             label: "Normal service",
             data: normalData,
             backgroundColor: 'rgb(75, 192, 192)',
            }
        ]   
      }
    }
    height ={300}
    width ={600}
    
    options={
      {
        maintainAspectRatio: true,

        scales: {
          yAxes: [{
            scaleLabel: {
              display: true,
              labelString: yAxis
            }
          }], 
          xAxes:[{
            scaleLabel: {
              display: true,
              labelString: 'Run No.'
            }
          }]
        }

    
    }
    
  
  } 
    />
    
    
    
    
    </>
  );
}

export default LineChart