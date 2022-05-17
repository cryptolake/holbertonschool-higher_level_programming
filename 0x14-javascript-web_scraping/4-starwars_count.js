#!/usr/bin/node
const axios = require('axios');
axios.get(process.argv[2], {
  headers: {
    Accept: 'application/json'
  }
})
  .then(resp => {
    let charCount = 0;
    const films = resp.data.results;
    const character = 'https://swapi-api.hbtn.io/api/people/18/';
    for (let i = 0; i < films.length; i++) {
      if (films[i].characters.indexOf(character) > -1) {
        charCount += 1;
      }
    }
    console.log(charCount);
  });
