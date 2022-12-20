#!/usr/bin/node

const argv = process.argv;
argNum = Number(argv[1]);
if (argNum) {
  console.log(argNum);
} else {
  console.log('Not a number');
}
