import {useEffect} from 'react'

function Display({ lives, win }) {    
  
    const imgSetter = () => {
    console.log('set image')
    console.log(win)
    if (win === true) {
        return "win"
    }else{
    return lives
    }
  }


    return (
      <img className='border-4 w-1/2 rounded-xl border-black opacity-50'src={`./src/assets/imgs/${imgSetter()}.png`}/>
      
    )
  }
  
  export default Display
  