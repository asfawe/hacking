var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');

// nano는 text에딧터가 아니다 ㅋㅋㅋㅋ nano는 Couchdb와 상화작용할 수 있게 만들어진 Couchdb 클라이언트 라이브러리다.
const nano = require('nano')(`http://${process.env.COUCHDB_USER}:${process.env.COUCHDB_PASSWORD}@couchdb:5984`); // Couchdb와 연결
const users = nano.db.use('users'); // users의 데이터베이스를 사용하는 거임.
var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views')); // 말 그래도 app의 views를 __dirname의 views로 바꾼다는 거다.
// 조금더 순화해서 말을 해보자면 원래 flask에서 templates안에 index.html을 넣어야 페이지가 로딩이 되었잖아? 근데 내가 index.html 같은 파일들을
// templates가 아닌 views 폴더 안에서 관리하고 싶으면 위에처럼 바꾸면 된다는 거다. flask에서는 다르겠지만...  
app.set('view engine', 'ejs'); // view engine을 ejs로 설정한다는 거고

app.use(express.json()); //  클라이언트로 부터 받은 http 요청 메시지 형식에서 body데이터를 해석하기 위해서 express.json()와 
app.use(express.urlencoded({ extended: false })); // express.urlencoded()로 처리가 필요합니다.
app.use(cookieParser()); // 요청된 쿠키를 쉽게 추출할 수 있도록 도와주는 미들웨어 입니다. express의 request(req) 객체에 cookies 속성이 부여됩니다.
app.use(express.static(path.join(__dirname, 'public'))); // 웹에서 접근가능한 공간을 정해주는 거다.

/* GET home page. */
app.get('/', function(req, res, next) {
  res.render('index');
});

/* POST auth */
app.post('/auth', function(req, res) {
    users.get(req.body.uid, function(err, result) {	 // users데이터 베이스에서 user의 id를 가져온다. 여기서 Cou
        if (err) {
            console.log(err);
            res.send('error');
            return;
        }
        if (result.upw === req.body.upw) {
            res.send(`FLAG: ${process.env.FLAG}`);
        } else {
            res.send('fail');
        }
    });
});

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;