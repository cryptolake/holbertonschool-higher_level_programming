#!/usr/bin/node
let ancArr = require('./100-data.js').list;
console.log(ancArr);
ancArr = ancArr.map((x, y) => x * y);
console.log(ancArr);
