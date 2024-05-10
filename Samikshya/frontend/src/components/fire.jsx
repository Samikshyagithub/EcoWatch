import React from 'react';

const ImageDisplay = ({ image, caption }) => {
  return (
    <div className="image-container">
      <img className="image" src={image} alt={caption} />
      <div className="caption">{caption}</div>
    </div>
  );
}

export default ImageDisplay;