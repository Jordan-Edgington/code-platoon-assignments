import { useState, useEffect } from 'react'
import { useNavigate, useOutletContext } from 'react-router-dom'
import axios from 'axios'
import Card from 'react-bootstrap/Card';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';

function CharactersPage() {

  const {checkIfFavorite, removeFromFavorites, addToFavorites} = useOutletContext()

  const [characters, setCharacters] = useState([])
  const navigate = useNavigate();
  useEffect(() => {
    const getCharacters = async () => {
      const response = await axios.get('https://rickandmortyapi.com/api/character')
      setCharacters(response.data.results)
      console.log(response.data.results)
    }
    getCharacters()
  }, [])

  const goToChar = (id) => {
    navigate(`/character/${id}/`)
  }

    return (
      <>

      <ul className='p-4 m-4'>
        <Row xs={1} sm={1} md={2} lg={3} className="g-4">
        {
          characters.map(char => <li key={char.id}>
            <Card border='info' style={{width: '24rem', height: '13rem'}}><Card.Body>
              <Row xs={2}>
              <img src={char.image}/>
              <ul className='p-2 '>
              {checkIfFavorite(char) ? <Button variant='outline-success' size='xs' onClick={()=>{removeFromFavorites(char)}}>Unfavorite</Button> : <Button variant='outline-success' size='xs' onClick={()=>{addToFavorites(char)}}>Favorite</Button>} 
                <br/>
                <li>Name: {char.name}</li>
                <li>Gender: {char.gender}</li>
                <br/>
                <Button variant='outline-success' size='xs' onClick={()=> goToChar(char.id)} >More Details</Button>
              </ul>
              </Row>
            </Card.Body></Card>
          </li>)
        }
        </Row>
        </ul>
        <Row xs={3}>
          <div></div>
        <div className='pagesContainer'><Button variant='success' size='md' className='pagesButton'>Prev.</Button><Button variant='success' size='md'>Next</Button></div>
        <div></div>
        </Row>
      </>
    )
  }
  
  export default CharactersPage