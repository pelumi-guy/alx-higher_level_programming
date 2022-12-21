#!/usr/bin/node

const theDict = require('./101-data').dict;
const myDict = {};

for (const each of Object.values(theDict)) {
  myDict[each] = [];
}

for (const each of Object.keys(theDict)) {
  myDict[theDict[each]].push(each);
}

console.log(myDict);
