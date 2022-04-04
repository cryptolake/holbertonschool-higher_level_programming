#!/usr/bin/node
const { argv } = require('process');

if (!argv[2] || isNaN(argv[2])) {
  console.log('Missing size');
} else {
  let tile = '';
  for (let j = 1; j <= argv[2]; j++) {
    tile += 'X';
  }
  for (let i = 1; i <= argv[2]; i++) {
    console.log(tile);
  }
}
