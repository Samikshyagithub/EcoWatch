import React from 'react';
import ImageDisplay from '../components/fire'; // Adjust the path to the ImageDisplay component
import House from "../assets/House.jpg";

const FireDetection = () => {
  return (
    <div className="App">
      <ImageDisplay image={House} caption="Your caption here" />
    </div>
  );
}

export default FireDetection;