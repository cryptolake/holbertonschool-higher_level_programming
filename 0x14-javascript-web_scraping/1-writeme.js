#!/usr/bin/node
const fs = require('fs');
const data = process.argv[3];

try {
  fs.writeFileSync(process.argv[2], data);
} catch (err) {
  console.log(err);
}
