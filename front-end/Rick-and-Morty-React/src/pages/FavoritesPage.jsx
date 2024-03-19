import { useState, useEffect } from 'react'
import { useNavigate, useOutletContext } from 'react-router-dom'
import Card from 'react-bootstrap/Card';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';

function FavoritesPage() {
    const {checkIfFavorite, removeFromFavorites, addToFavorites, favorites} = useOutletContext()
    const [characters, setCharacters] = useState(favorites)

    const navigate = useNavigate();
    const goToChar = (id) => {
    navigate(`/character/${id}/`)
  }

  useEffect(() => {
    setCharacters(favorites)
  }, [favorites])

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
      </>
    )
  }
  
  export default FavoritesPage