#!/usr/bin/node
const axios = require('axios');
const fs = require('fs');
const file = process.argv[3];

axios.get(process.argv[2])
  .then(resp => {
    const data = resp.data;

    try {
      fs.writeFileSync(file, data);
    } catch (err) {
      console.log(err);
    }
  });
