#!/usr/bin/node

/**
 * Script to query `https://swapi-api.alx-tools.com/api/films/` API endpoint
 */

const request = require('request');

const URL = 'https://swapi-api.alx-tools.com/api/films';

function fetchJSON (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (err, res, body) => {
      if (err) {
        return reject(err);
      }
      resolve(body);
    });
  });
}

async function main (movieId) {
  try {
    const data = await fetchJSON(`${URL}/${movieId}`);
    if (!data.characters) {
      return;
    }
    for (const character of data.characters) {
      const characterData = await fetchJSON(character);
      console.log(characterData.name);
    }
  } catch (error) {
    console.log(error.message);
  }
}

main(process.argv[2]);
