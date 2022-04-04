#!/usr/bin/node
const { argv } = require('process');

if (!argv[2] || isNaN(argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argv[2]);
}
