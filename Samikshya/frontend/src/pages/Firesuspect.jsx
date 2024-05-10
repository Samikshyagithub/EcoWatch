import React, { useState, useEffect } from 'react';
import axios from '../axios-config'; 
import Sidebar from '../components/Sidebar';

function FireSuspect() {
  const [imageUrls, setImageUrls] = useState([]);

  useEffect(() => {
    // Fetch image URLs from Flask endpoint
    axios.get('/getsuspects')
      .then(response => {
        // Set the image URLs in state
        setImageUrls(response.data.image_urls);
      })
      .catch(error => {
        console.error('Error fetching image URLs:', error);
      });
  }, []);

  return (
    <div className="flex w-full h-screen">
      <div className="w-[18%]">
        <Sidebar />
      </div>
    <div style={{ textAlign: "center" }}>
  <h1 style={{ fontWeight: "bold", fontFamily: "Arial, sans-serif", textDecoration: "underline", marginTop:"50px" ,marginBottom: "50px",fontSize: "2.5em" }}>Suspects</h1>
  <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: "10px" }}>
    {imageUrls.map((imageUrl, index) => (
      <div key={index} style={{ width: "100%", height: "100%", overflow: "hidden", borderRadius: "8px" }}>
        <img src={imageUrl} alt={`Suspect ${index}`} style={{ width: "100%", height: "100%", objectFit: "cover" }} />
      </div>
    ))}
  </div>
</div>
</div>
  );
}

export default FireSuspect;