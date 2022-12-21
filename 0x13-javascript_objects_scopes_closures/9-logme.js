#!/usr/bin/node

let count = -1;
exports.logMe = function (item) {
  count++;
  return console.log(`${count}: ${item}`);
};
