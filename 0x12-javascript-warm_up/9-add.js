#!/usr/bin/node
const { argv } = require('process');

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

if (!argv[2] || isNaN(argv[2]) || !argv[3] || isNaN(argv[3])) {
  console.log('NaN');
} else {
  console.log(add(argv[2], argv[3]));
}
