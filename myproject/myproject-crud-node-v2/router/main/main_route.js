const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
	res.cookie("cookie", "hahaha");
	res.render('index', {http: "GET"});
});

router.post('/', (req, res) => {
	res.render('index', {http : "POST"});
});

router.get('/hehe', (req, res) => {
	res.json({
		report: "hahaha"
	  }).status(200);
	console.log(res.statusCode);
	console.log(res.statusCode);
	console.log(res.statusCode);
});

router.get('/haha/:id' , (req, res) => {
	console.log(req.params.id);
	res.send(req.params.id);
});

module.exports = router;