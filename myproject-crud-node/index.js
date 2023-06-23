const express = require('express');

const app = express();

app.get('/', function(req, res) {
	console.log("Hello, world!");
})

app.listen(8080, () => {
	console.log("Hello, world!!!!!!!!!!!");
});