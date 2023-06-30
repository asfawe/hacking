const express = require('express');
const router = express.Router();
let a, b;
const getTime = () => {
	let today = new Date();
	let hours = today.getHours();
	let minutes = today.getMinutes();
	let seconds = today.getSeconds();
	let milliseconds = today.getMilliseconds();
	return (
	  String(hours) + String(minutes) + String(seconds) + String(milliseconds)
	);
  };

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

router.get('/lala', (req, res)=>{
	setTimeout(() => {
		a = getTime();
	  }, 1000);
	  console.log(a);
	  res.send(a);
});

router.get('/hoho' , (req, res) => {
console.log(b);
	res.send(getTime());
});
module.exports = router;

console.log(a);
console.log(b);