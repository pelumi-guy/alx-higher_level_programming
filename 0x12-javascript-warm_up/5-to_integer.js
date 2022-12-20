#!/usr/bin/node

const argv = process.argv;
const argNum = Number(argv[2]);

if (argNum) {
  console.log('My number:', argNum);
} else {
  console.log('Not a number');
}
