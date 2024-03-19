import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"
import image from '../assets/imgs/error.jpeg'
function HomePage() {

    return (
      <>
        <Row style={{margin:'50px'}}>
            <Col> </Col>
            <Col> <h1>The page you are looking for does not exist...</h1></Col>
            <Col></Col>
        </Row>
        <Row style={{margin:'50px'}}>
            <Col align='center'>
            <img id="error" src={image}/>
        </Col>
        </Row>
      </>
    )
  }
  
  export default HomePage