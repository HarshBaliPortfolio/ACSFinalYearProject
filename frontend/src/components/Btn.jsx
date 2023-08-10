import React from 'react'

export const Btn = ({text, color, onClick}) => {
  return ( <button style ={{backgroundColor: color , color : 'white'}}  
  onClick ={onClick}  className='btn btn-block'>{text}</button>
  );
}
