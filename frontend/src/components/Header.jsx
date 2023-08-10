
import FormButton from './FormButton';
import { FaCaretLeft, FaHospital } from 'react-icons/fa';

const Header = ({title, home, onBackClick, onAdd, buttonVal, inputButton}) => {
  return (
 <header className='header'>
   {/* if title is not department then show back sign */}
    {title !== 'Departments' && <FaCaretLeft  className={'icons'} onClick={onBackClick}/> }
    <h1>{title} </h1>

    {/* if title is not departments then  */}
    {title !== 'Departments' && <FaHospital className={'icons'} onClick={home}/>}
     
     {inputButton && <FormButton color ={buttonVal? 'red' :'blue'}  buttonVal ={buttonVal}onClick={onAdd}/>}

 </header>
  );
};




export default Header;
