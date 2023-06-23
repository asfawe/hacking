const express = require('express');
const mongoose = require('mongoose');
const app = express();
const User = require('./models/User');
const port = 3000;
require('dotenv').config({path:'variables.env'}); // dotenv 파일이 어디있냐? 바로 variable.env 파일 안에 있다.

app.use(express.static('./images/'));

app.get('/', function (req, res) {
	return res.sendFile(__dirname + "/templates/index.html");
});

// app.get('/', (req, res) => {
// 	const newUser = new User();
// 	newUser.name = "Ecen2033";
// 	newUser.email = "Ecen2033@gmail.com";
// 	newUser.age = 20;
// 	newUser.save()
// 	.then((user) => {
// 		console.log(user);
// 		res.json({
// 			message: 'User Created Successfully',
// 		})
// 	})
// 	.catch((err) => {
// 		res.json({
// 			message: err.toString(),
// 		});
// 	});
// });

app.listen(port, (err) => {
	if (err) {
		return console.error(err);
	} else {
		mongoose.connect(process.env.mongodb_url, { useNewUrlParser: true})
		.then(() => {
			console.log('Connected to the database successfully');
		})
		.catch((err) => {
			console.error('Failed to connect to the database:', err);
		});
	}
});
