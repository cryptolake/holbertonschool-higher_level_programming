#!/usr/bin/node
exports.converter = function (base) {
  function convFrom10 (num) {
    // if (Math.floor(num / base) === 0) {
    //   if (num % base >= 10) {
    //     return String.fromCharCode(97 + (num % base) - 10);
    //   }
    //   return (num % base).toString();
    // }
    // if (num % base >= 10) {
    //   return convFrom10(Math.floor(num / base)) + String.fromCharCode(97 + (num % base) - 10);
    // }
    // return convFrom10(Math.floor(num / base)) + (num % base).toString();
    // TURNS OUT ALL OF THIS IS UNNECESARRY HAHA
    return num.toString(base);
  }
  return convFrom10;
};
