#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newdict = {};
for (const key in dict) {
  if (newdict[dict[key].toString()]) {
    newdict[dict[key].toString()].push(key);
  } else {
    newdict[dict[key]] = [key];
  }
}
console.log(newdict);
