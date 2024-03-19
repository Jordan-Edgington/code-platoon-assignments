/* eslint-disable react/no-unescaped-entities */
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"

function HomePage() {

  return (
    <>
      <Row>
        <Col align='center'>
          <div className="article">
            <p> "If you want to experience mind-bending sci-fi adventures, thought-provoking philosophical discussions, and a dash of dark humor that will leave you questioning your own existence, then buckle up for the wild ride that is Rick and Morty!" <br></br> -ChatGPT</p>
          </div>
          <div className="article">
            <p>
              "Watching Rick and Morty is like debugging code - it challenges you to think outside the box and pushes the boundaries of what you thought was possible." <br></br> -Francisco (Not really)
            </p>
          </div>
        </Col>
        <Col>
          <img id='homePic' src='./src/assets/imgs/rick.png' width='60%' border='2px solid black' />
        </Col>
      </Row>
    </>
  )
}

export default HomePage