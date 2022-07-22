import React from 'react'
import Description from './description';
import FileUploader from './fileUploader';
import NavBar from './navbar';
import {ToastContainer} from 'react-toastify';
import Footer from './footer';
function Home() {
  return (
    <>
      <NavBar/>
      <Description/>
      <FileUploader/>
      <ToastContainer/>
    <Footer/>
    </>)
}

export default Home