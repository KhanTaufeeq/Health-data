import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';

function GetBP() {

  const [listBP, setListBP] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/bp/')
        .then((response) => {
          console.log(response.data);
          setListBP(response.data)
        })
        .catch((error) => {
          console.log(error);
        })
  }, [])
  
  return (
    <>
      <div className="show-bp-div">
        <h1>BP</h1>
        {
          listBP.map(bp => {
            return(
              <div className="bp-list" key={bp.id}>
                <p>{bp.timing}</p>
                <h2>Systolic: {bp.systolic}</h2>
                <h2>Diastolic: {bp.diastolic}</h2>
              </div>
            )
          })
        }
      </div>
    </>
  )
}

export default GetBP