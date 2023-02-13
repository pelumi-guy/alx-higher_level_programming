#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const l = (a) => console.log(a);

request
  .get(url, (err, res, body) => {
    if (err) {
      l(err);
    } else {
      const info = JSON.parse(body);

      let count = 0;
      for (const result of info.results) {
        if (result.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          count++;
        }
      }
      l(count);
    }
  });
