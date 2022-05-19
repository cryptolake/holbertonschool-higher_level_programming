#!/usr/bin/node
const axios = require('axios');
axios.get(process.argv[2])
  .then(resp => {
    let charCount = 0;
    const films = resp.data.results;
    const character = 18;
    for (let i = 0; i < films.length; i++) {
			for (let c in films[i].characters) {
				if (films[i].characters[c].includes(character)) {
					charCount += 1;
				}
			}
    }
    console.log(charCount);
  });
