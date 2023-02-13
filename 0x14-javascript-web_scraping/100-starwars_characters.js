#!/usr/bin/node

const request = require('request');
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
const l = (a) => console.log(a);

const sendRequest = async (url) => {
  return new Promise((resolve, reject) => {
    request.get(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

try {
  sendRequest(movieUrl)
    .then((res) => {
      try {
        for (const character of res.characters) {
          sendRequest(character)
            .then((person) => l(person.name));
        }
      } catch (err) {
        l(err);
      }
    });
} catch (err) {
  l(err);
}
