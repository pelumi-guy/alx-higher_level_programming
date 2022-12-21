#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const each of list) {
    if (each === searchElement) count++;
  }
  return count;
};
