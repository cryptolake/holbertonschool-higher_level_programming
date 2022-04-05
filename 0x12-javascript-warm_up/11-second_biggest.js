#!/usr/bin/node
const { argv } = require('process');

if (argv.length < 4) {
  console.log(0);
} else {
  let argints = argv.slice(2, argv.length);
  argints = argints.map(n => parseInt(n));
  argints.sort((a, b) => a - b);
  console.log(argints[argints.length - 2]);
}
