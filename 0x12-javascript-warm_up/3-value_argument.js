#!/usr/bin/node

const argv = process.argv;
if (argv[1]) {
  console.log(argv[1]);
} else {
  console.log('No argument');
}
