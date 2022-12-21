#!/usr/bin/node
const PrevSquare = require('./5-square');

module.exports = class Square extends PrevSquare {
  charPrint (c) {
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += c === undefined ? 'X' : c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
};
