import fetch from 'node-fetch';
import express from 'express';
const router = express.Router();


let jsonData;

async function fetchData() {
  try {
    var url = "http://localhost:5000/vitals/datastore";

    // Make a GET request using fetch and return a Promise
    return fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        throw error; // Re-throw the error to be caught by the caller
      });
  } catch (error) {
    console.error('Error:', error);
    throw error; // Re-throw the error to be caught by the caller
  }
}

// Call fetchData function and handle the result using async/await
async function main_get() {
  try {
    const resp = await fetchData();
    console.log(resp);
  } catch (error) {
    console.error('An error occurred:', error);
  }
}

// Call the main function to start the execution

async function postData() {
  try {
    const url = "http://localhost:5000/vitals/datastore";

    const postData = {
      patient_id: 1, 
      sys_bp: 120,
      dia_bp: 80,
      weight_lbs: 150,
      height_inches: 70
    };

    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(postData)
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    return await response.json();
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}

async function main_post() {
  try {
    const resp = await postData();
    console.log(resp);
  } catch (error) {
    console.error('An error occurred:', error);
  }
}

// save as variables 
// main_post()
// main_get() 