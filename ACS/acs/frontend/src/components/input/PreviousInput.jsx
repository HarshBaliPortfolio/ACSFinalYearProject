const PreviousInput = ({input, onInputClick, onSimuClick}) => {
  return (<div className='option' onDoubleClick={()=>{onInputClick(input.id)}} onClick={()=>onSimuClick(input.id)}   >
    <h3>{input.id}</h3>

 </div>
  );
}

export default PreviousInput