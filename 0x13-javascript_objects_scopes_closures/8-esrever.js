#!/usr/bin/node
exports.esrever = function (list) {
  rev = []

  for (let i = list.length - 1; i >= 0; i--) {
    rev[list.length - 1 - i] = list[i]
  }
  return rev;
};
