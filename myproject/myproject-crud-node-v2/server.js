const express = require('express');
const logger = require('morgan');
const main_router = require('./router/main/main_route');
const app = express();

app.set('view engine', 'ejs');
app.set("views", __dirname + "/pages/html");

app.use(logger("dev")); // GET / 304 5.973 ms - - http 요청 볼 수 있음 😳

app.use(function (req, res, next) {
	// res.setHeader("Access-Control-Allow-Origin", "example.com");
	res.setHeader("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE");
	res.setHeader(
		"Access-Control-Allow-Headers",
		"X-Requested-With,content-type, Authorization"
	);
	next();
});

app.use("/", main_router);

app.use(function (req, res, next) {
	var err = new Error("Page Not Found");
	err.status = 404;
	next(err);
});

// 개발 모드에서는 에러 메시지에 에러 상세 정보를 추가
if (app.get('env') === 'development') {
	app.use(function (err, req, res, next) {
		res.status(err.status || 500);
		res.render('error', { message: err.message, error: err });
	});
}

// 프로덕션 모드에서는 에러 메시지만 전달
app.use(function (err, req, res, next) {
	res.status(err.status || 500);
	res.render('error', { message: err.message });
});


app.listen(3000, (err) => {
	if (err) {
		console.error(err);
	} else {
		console.log('listening on port');
	}
});