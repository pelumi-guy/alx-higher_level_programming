#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
const l = (a) => console.log(a);

request
  .get(url, (err, res, body) => {
    if (err) {
      l(err);
    } else {
      l(JSON.parse(body).title);
    }
  });
