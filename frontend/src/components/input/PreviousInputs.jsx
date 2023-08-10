import PreviousInput from "./PreviousInput";

const PreviousInputs = ({ inputs, onInputClick, onSimuClick }) => {
   
  return( 
  <>
    {
       inputs.map((input)=>(
        <PreviousInput key= {input.id} input = {input} onInputClick={onInputClick} onSimuClick={onSimuClick}/>
        )) }
  </>);
};

export default PreviousInputs;
 