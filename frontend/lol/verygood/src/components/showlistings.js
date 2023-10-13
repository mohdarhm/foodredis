import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from './card';

function ShowListings() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Make a POST request with source_id=8
    axios
      .post('http://localhost:8000/api/get_card_data/', { source_id: 8 })
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
        setLoading(false);
      });
  }, []);

  return (
    <div className='cards-container'>
      {loading ? (
        <p>Loading...</p>
      ) : (
        data.map((item, index) => (
          <Card
            key={index} // You should use a unique identifier as the key, not index
            data={item} // Pass the data for the card as a prop
          />
        ))
      )}
    </div>
  );
}

export default ShowListings;
