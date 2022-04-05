#!/usr/bin/node
let l = 0;
exports.logMe = function (item) {
  console.log(`${l}: ${item}`);
  l += 1;
};
