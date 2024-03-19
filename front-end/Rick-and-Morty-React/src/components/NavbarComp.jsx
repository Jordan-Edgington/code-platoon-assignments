import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { Link } from 'react-router-dom'
import Button from 'react-bootstrap/Button'

function BasicExample() {
  return (
    <Navbar expand="lg" className="bg-body-tertiary" data-bs-theme='dark'>
      <Container>
        <Navbar.Brand><Link to='/'><Button variant='outline' size='lg' style={{margin: '1rem'}}>Rick and Morty</Button></Link></Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Link to='aboutus/'><Button className="headerbutton" variant='success' >About</Button></Link>
            <Link to='characters/'><Button className="headerbutton" variant='success'>Characters</Button></Link>
            <Link to='favorites/'><Button className="headerbutton" variant='success'>Favorites</Button></Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default BasicExample;