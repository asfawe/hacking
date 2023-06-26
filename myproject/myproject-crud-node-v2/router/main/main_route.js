const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
	res.cookie("cookie", "hahaha");
	res.render('index', {http: "GET"});
});

router.post('/', (req, res) => {
	res.render('index', {http : "POST"});
});

module.exports = router;