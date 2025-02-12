import Header from './Header.jsx'
import Footer from './Footer.jsx'
import Food from './Food.jsx'
import Card from './Card.jsx'
import Button from './Button/Button.jsx'
import Student from './Student.jsx'
import List from './List.jsx'

function App() {
  return(
    <>
      <Header/>
      <Food/>
      
      <Student 
      name="Patrick"/>
      
      <Card
      name="Tshepiso"
      position="photographer"/>

      <Card
      name="Esaya"
      position="Producer"/>
      <Button />
      <Footer/>
      <List/>
    </>
  ); 
}

export default App
