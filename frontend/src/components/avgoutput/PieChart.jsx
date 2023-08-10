import {Pie} from "react-chartjs-3";





const PieChart = ({ lDVisits, sDVisits , dLDVisits, dSDVisits }) => {
 
  return (<>
  <Pie
    data =
    {
      {
        labels: [
            'On Typical Longest Day',
            'On Typical Shortest Day',
            'On Digitalised Longest Day',
            'On Digitalised Shortest Day',

        ],
        datasets : 
        [{
            label: 'My First Dataset',
            data: [lDVisits, sDVisits, dLDVisits,dSDVisits],
            backgroundColor: [
                'rgb(75, 192, 192)',
              'rgb(54, 162, 235)',
              'rgb(255, 99, 132)',
              'rgb(255,0,0)'
            ],
            hoverOffset: 4
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

export default PieChart