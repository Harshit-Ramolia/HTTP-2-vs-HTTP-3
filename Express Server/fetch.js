// const fetch = require('node-fetch');
import fetch from "node-fetch";
fetch('https://google.com')
    .then(response => {
        console.log(response.text())
    })
    .catch(error => {
        console.log(error)
    });
