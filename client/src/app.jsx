import './app.css';
import 'react-toastify/dist/ReactToastify.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Home from './components/home';
import Similarity from './components/similarity';
import Elegance from './components/elegance';
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" exact element={<Home/>}/>
        <Route path="/similar" element={<Similarity/>}/>
        <Route path="/elegant" element={<Elegance/>}/>
      </Routes>
    </BrowserRouter>  
  )

}

export default App;
