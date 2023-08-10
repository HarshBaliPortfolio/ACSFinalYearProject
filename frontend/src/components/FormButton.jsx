import { FaPlusSquare, FaMinusSquare } from 'react-icons/fa';


const FormButton = ({color, onClick, buttonVal}) => {


  return (
    <>
      {buttonVal ? <FaMinusSquare className='plusMinus' style={{color:color}} onClick={onClick} />
   
      :  
       <FaPlusSquare  className='plusMinus' style={{color:color}} onClick={onClick} /> 
      }

      </> );

};


export default FormButton;
