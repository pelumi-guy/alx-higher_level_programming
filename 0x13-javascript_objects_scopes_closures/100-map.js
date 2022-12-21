#!/usr/bin/node

const theList = require('./100-data').list;
const mappedList = theList.map((each, i) => each * i);

console.log(theList);
console.log(mappedList);
