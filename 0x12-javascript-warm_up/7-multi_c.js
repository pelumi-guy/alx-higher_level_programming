#!/usr/bin/node

const argv = process.argv;
const argNum = Number(argv[2]);

if (argNum) {
  for (let i = 0; i < argNum; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
