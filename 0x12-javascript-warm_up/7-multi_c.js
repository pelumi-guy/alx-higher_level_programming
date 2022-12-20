#!/usr/bin/node

const argv = process.argv;
argNum = Number(argv[1]);
if (argNum) {
  for (let i = 0; i < argNum; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
