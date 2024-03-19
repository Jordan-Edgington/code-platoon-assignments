import { useState, useEffect } from 'react'
import { useParams, useOutletContext } from 'react-router-dom'
import axios from 'axios'
import Card from 'react-bootstrap/Card';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';

function CharacterPage() {
  const [character, setCharacter] = useState({})
  const { id } = useParams()
  const {checkIfFavorite, removeFromFavorites, addToFavorites} = useOutletContext()

  
  useEffect(() => {
    const getCharacter = async () => {
      const response = await axios.get(`https://rickandmortyapi.com/api/character/${id}`)
      setCharacter(response.data)
    }
    getCharacter()
  }, [])



    return (
      <>
      <ul className='p-4 m-4'>
        <Row xs={1} sm={2} md={3} lg={4} className="g-4">
            <Card border='info' style={{width: '34rem', height: '16rem'}}><Card.Body>
              <Row xs={2}>
              <img src={character.image} />
              <ul className='d-flex p-2 '>
                <Row xs={1}>
                <li>Name: {character.name}</li>
                <li>Gender: {character.gender}</li>
                <li>Species: {character.species}</li>
                {character.origin && 
                <li>Origin: {character.origin.name}</li>}
                {checkIfFavorite(character) ? <Button variant='outline-success' size='xs' onClick={()=>{removeFromFavorites(character)}}>Unfavorite</Button> : <Button variant='outline-success' size='xs' onClick={()=>{addToFavorites(character)}}>Favorite</Button>} 

                {/* {console.log(character.origin.name)}
                <li>Origin: {character.origin.name}</li> */}
                </Row>
              </ul>
              </Row>
            </Card.Body></Card>
        </Row>
        </ul>
      </>
    )
  }
  
  export default CharacterPage