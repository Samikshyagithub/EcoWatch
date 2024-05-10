import React, { useState, useEffect } from 'react';
import axios from '../axios-config'; // Import axios instance with configured settings

function Suspects() {
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
    <div>
      <h1>Suspects</h1>
      <div className="image-grid">
        {imageUrls.map((imageUrl, index) => (
          <img key={index} src={imageUrl} alt={`Suspect ${index}`} />
        ))}
      </div>
    </div>
  );
}

export default Suspects;
