#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w == null || h == null) return;

    this.width = w;
    this.height = h;
  }

  print () {
    let row = 'X';
    for (let i = 1; i < this.width; i++) {
      row += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
