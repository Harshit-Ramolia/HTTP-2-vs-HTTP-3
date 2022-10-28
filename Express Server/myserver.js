const express = require("express"),
  app = express(),
  bodyParser = require('body-parser');

const path = require('path');
app.use(express.static('public'))

app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(bodyParser.json());


app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, 'htmltest.html'));
});


app.listen(3000, () => {
  console.log("App is running at port 3000");
});