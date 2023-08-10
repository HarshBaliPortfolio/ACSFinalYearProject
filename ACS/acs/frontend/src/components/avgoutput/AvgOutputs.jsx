import AvgOutput from "./AvgOutput";

const AvgOutputs = ({ avgOutputs }) => {

  return( 
  <>
  
        <div className='results'       >
          <h1>As Is</h1>
        {
          avgOutputs.filter((avgOutput) =>(!avgOutput.is_digital)).map((avgOutput)=>(
           < AvgOutput key= {avgOutput.id} avgOutput= {avgOutput} />
           ))}
        </div>

        <div className='results'       >
          <h1>Digital</h1>
          {avgOutputs.filter((avgOutput) =>(avgOutput.is_digital)).map((avgOutput)=>(
            < AvgOutput key= {avgOutput.id} avgOutput= {avgOutput} />

            ))}
          </div>
      
     

  </>);
};

export default AvgOutputs;
 