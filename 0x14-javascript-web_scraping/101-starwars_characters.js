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
      const characters = res.characters;
      try {
        for (let i = 0; i < characters.length; i++) {
          sendRequest(characters[i])
            .then((person) => l(person.name));
        }
      } catch (err) {
        l(err);
      }
    });
} catch (err) {
  l(err);
}
