#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let row = c ? c : 'X';
    for (let i = 1; i < this.width; i++) {
      row += c ? c : 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
};
