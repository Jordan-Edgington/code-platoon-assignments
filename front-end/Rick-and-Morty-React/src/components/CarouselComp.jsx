import { useState, useEffect } from 'react'
import axios from 'axios'
import Carousel from 'react-bootstrap/Carousel';
import Img from '../assets/imgs/banner.png'

function UncontrolledExample() {
    const [episodes, setEpisodes] = useState([])

    useEffect(() => {
        const getEpisodes = async () => {
          const response = await axios.get('https://rickandmortyapi.com/api/episode')
          setEpisodes(response.data.results)
          console.log(response.data.results)
        }
        getEpisodes()
      }, [])

  return (
    <Carousel>
        {episodes.map((episode) => 
        <Carousel.Item key={episode.id}>
            <img id='banner' className='d-block w-60' src={Img} alt='slide' width='100%' height='50%'/>
            <Carousel.Caption>
                <h3 className='bannertext'>{episode.name}</h3>
                <p className='bannertext'>{episode.air_date} <br></br>{episode.episode} <br></br>{episode.created}</p>
            </Carousel.Caption>
        </Carousel.Item>)}
    </Carousel>
  );
}

export default UncontrolledExample;