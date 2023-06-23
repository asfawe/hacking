const express = require('express');
const mongoose = require('mongoose');
const User = require('./models/User');
const Comment = require('./models/Comment');
const session = require('express-session');
const bcrypt = require('bcrypt');
const app = express();
const port = 3000;
require('dotenv').config({path:'variables.env'}); // dotenv 파일이 어디있냐? 바로 variable.env 파일 안에 있다.

app.use(express.urlencoded({ extended: true }));
app.use(express.static('./public/'));
app.use('/404', function(req, res) {
    res.status(404);
    return res.sendFile(__dirname + "/views/404.html"); // 여기서 404.html은 위에서 작성한 404 페이지 HTML 파일입니다.
});
app.set('view engine', 'ejs');
app.use(session({
	secret: process.env.session_key,  // 비밀 키를 입력합니다. 이 키는 세션 id를 암호화하기 위해 사용됩니다.
	resave: false,  // 세션을 강제로 저장할지 여부를 설정합니다. 변경되지 않아도 항상 저장할 것인지를 결정합니다.
	saveUninitialized: true,  // 세션이 필요하기 전까지는 세션을 생성하지 않습니다. 
  }));
app.get('/', function (req, res) {
	return res.sendFile(__dirname + "/views/index.html");
});

app.get('/signup', (req, res) => {
	return res.sendFile(__dirname + "/views/signup.html");
});

app.post('/signup', async (req, res) => {
	const { email, password, username, confirmation_password } = req.body;
	const exists = await User.exists({ $or: [{ username }, { email }] });

	if (password != confirmation_password) {
		return res.redirect('/404');
	}
	if (exists) {
		return res.redirect('/404');
	}

	try {
		await User.create({
			username: username,
			email: email,
			password: password,
		});
		return res.redirect('/');
	} catch (err) {
		return res.redirect('/404');
	};
});

app.get('/signin', (req, res) => {
	return res.sendFile(__dirname + "/views/signin.html");
});

app.post('/signin', async (req, res) => {
	const { username, password } = req.body;
  	const user = await User.findOne({ username : username });

	if (!user) {
		return res.redirect('/404');
	}
	const ok = await bcrypt.compare(password, user.password);
	if (!ok) {
		return res.redirect('/404');
	}
	req.session.loggedIn = true;
	req.session.user = user;
	return res.redirect("/");
});

app.get('/write', async (req, res) => {
	return res.sendFile(__dirname + "/views/write.html");
});

app.post('/write', async (req, res) => {
	const { title, description } = req.body;

	try {
		await Comment.create({
			title: title,
			description: description,
			user: req.session.user._id,
		});
		return res.redirect('/');
	} catch (err) {
		return res.redirect('/404');
	};
});

app.get('/read', async (req, res) => {
	const comments = await Comment.find({});
	return res.render('read', { comments: comments });
});

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
