const express = require('express');
const mongoose = require('mongoose');
const User = require('./models/User');
const Comment = require('./models/Comment');
const session = require('express-session');
const bcrypt = require('bcrypt');
const app = express();
const port = 3000;
const methodOverride = require('method-override');

require('dotenv').config({path:'variables.env'}); // dotenv 파일이 어디있냐? 바로 variable.env 파일 안에 있다.

app.use(express.urlencoded({ extended: true })); // 아주 중요한 것이여!! extended를 설정 안하면 Array, Object를 다 그냥 생으로 받음!!!!
app.use(methodOverride('_method'));
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
	try{
		const user = req.session.user;
		return res.render('index', {user:user});
	} catch(e) {
		return res.redirect('/404');
	}
	
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
			user: req.session.user,
			
		});
		return res.redirect('/');
	} catch (err) {
		return res.redirect('/404');
	};
});

app.get('/read', async (req, res) => {
	try {
		const user = req.session.user._id;

		if (!user) {
			return res.redirect('/404');
		}
		const comments = await Comment.find({}).populate('user');
		// populate('user')를 호출하여 각 댓글의 'user' 필드를 실제 User 객체로 대체합니다. 이렇게 하면 comment.user를 통해 사용자 정보에 직접 접근할 수 있습니다.
		
		return res.render('read', {comments: comments, user: user}); // 왜 comment를 중괄호로 감싸서 넘기나요? 자바스크립트에서는 중괄호를 객체를 정의할 때 사용합니다.
		// 아 그건 그렇고 그냥 res.render에서는 객체로 두번째 인자값을 받습니다. 그리고 객체로 넘겨줘야 ejs에서 접근을 할 수 있기 때문입니다.
		/* 만약 res.render('read', comments);와 같이 사용하면, EJS 템플릿에서는 comments라는 변수를 사용할 수 없고, 대신 comments 배열의 각 요소에 직접 접근해야 합니다. 이는 코드를 읽고 이해하는 데 복잡성을 더할 수 있습니다. */
	} catch (e) {
		return res.redirect('/404');
	}
	
});

app.get('/comments/edit/:id', async (req, res) => {
    const user = req.session.user._id;
    if (!user) {
        return res.redirect('/404');
    }
    try {
        const comment = await Comment.findById(req.params.id).populate('user');
        if (comment.user._id.toString() === user.toString()) {
            return res.render('edit', { comment: comment });
        } else {
            // 댓글의 작성자가 아닌 경우, 403 에러 페이지로 리다이렉트
            return res.redirect('/404');
        }
    } catch (error) {
        // 에러 발생 시, 에러 페이지로 리다이렉트
        return res.redirect('/404');
    }
});

app.put('/comments/edit/:id', async (req, res) => {
	const { title, description } = req.body;
	const user = req.session.user._id;

	if (!user) {
        return res.redirect('/404');
    }
    try {
        const comment = await Comment.findById(req.params.id).populate('user');
        if (comment.user._id.toString() === user.toString()) {
            await Comment.updateOne({_id: req.params.id}, {
                title: title,
                description: description
            });
            res.redirect('/read');
		}
    } catch (error) {
        // 에러 발생 시, 에러 페이지로 리다이렉트
        return res.redirect('/404');
    }
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
