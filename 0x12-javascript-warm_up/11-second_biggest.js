#!/usr/bin/node
const { argv } = require('process');

if (argv.length < 4) {
  console.log(0);
} else {
  const argints = argv.slice(2, argv.length);
  argints.sort();
  const secondlast = argints.length - 2;
  console.log(argints[secondlast]);
}
