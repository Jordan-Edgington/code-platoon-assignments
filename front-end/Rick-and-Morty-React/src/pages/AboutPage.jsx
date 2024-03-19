/* eslint-disable react/no-unescaped-entities */
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"
import CarouselComp from "../components/CarouselComp.jsx"

function AboutPage() {

  return (
    <>
      <Row>
        <Col align='center'>
          <div className="article">
            <p>
              "Rick and Morty" is an animated sci-fi comedy series that follows the adventures of an eccentric and brilliant scientist named Rick Sanchez and his  naive grandson Morty Smith. Together, they travel through different dimensions, galaxies, and alternate realities, encountering bizarre creatures and facing dangerous situations.

              The show explores themes of existentialism, morality, and the nature of reality while offering a satirical take on popular culture and science fiction tropes. Rick is portrayed as a nihilistic and alcoholic genius who is often reckless and selfish, while Morty serves as the moral compass, trying to navigate the chaotic universe they find themselves in.

              Throughout the series, Rick and Morty grapple with their complicated relationship, as well as the consequences of their actions on the various worlds they visit. The show also delves into the dynamics of their dysfunctional family, including Morty's parents, Jerry and Beth, and his sister, Summer.

              Despite its absurd and often dark humor, "Rick and Morty" has garnered critical acclaim for its clever writing, complex characters, and inventive storytelling. The series has developed a dedicated fanbase and has been praised for its intelligence, wit, and philosophical underpinnings.
            </p>
            <br></br>
            <h2>Episodes:</h2>
          </div>
        </Col>
      </Row>
      <Row>
        <CarouselComp></CarouselComp>
      </Row>
    </>
  )
}

export default AboutPage