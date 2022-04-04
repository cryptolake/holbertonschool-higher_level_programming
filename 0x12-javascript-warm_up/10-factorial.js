#!/usr/bin/node
const { argv } = require('process');

function factorial (num) {
  if (num == 1) {
    return num;
  }
  return num * factorial(num - 1);
}

if (!argv[2] || isNaN(argv[2])) {
  console.log(1);
} else {
  let num = parseInt(argv[2]); 
  console.log(factorial(num))
}
