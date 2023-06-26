const express = require("express");
const session = require("express-session");
const logger = require("morgan");
const cookieParser = require("cookie-parser");
const loginSession = require("./apis/session/session");
const adminReport = require("./apis/admin/admin_report");
const Router = require("./router/index/index_route");
const port = process.env.PORT || 8000;
const app = express();
const server = require("http").createServer(app);

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser("[**SECRET_KEY**]")); // cookie를 사용하는 이유는 jwt token을 쿠키에 저장하기 위해서 이다.

// session은 저장소다. 여기서 session을 어떻게 사용하는가? 라고 물어봤을 때
// 나는 이렇게 답하고 싶다. "jwt token을 쿠키에 담기위해서 사용한다."
// 결국에는 우리가 만든 session.js 는 jwt token을 생성하기 위해서 있는거다.
// jwt token은 그러면 언제 사용하나? 바로 인증할 때 많이 사용된다.
// 사용자 인증 결국에는 우리가 admin으로 로그인해서 들어가는게 목표이기 때문에
// 어찌어찌 jwt token을 admin으로 가져와야 한다.
app.use(
  session({
    resave: false,
    saveUninitialize: true, // 오타 같은디... saveUninitialize가 아니라 saveUninitialized 인것 같은데...
    secret: "[**SECRET_KEY**]",
    cookie: {
      httpOnly: true, // JavaScript를 통해 쿠키에 접근하는 것을 방지합니다. 
      secure: false, // 웹 브라우저는 쿠키를 HTTPS를 통해만 서버로 전송합니다. 
    },
    name: "cookie",
  })
);

app.use(function (req, res, next) {
  res.setHeader("Access-Control-Allow-Origin", "self"); // 이거 잘못된 코드임.
  // jwt token을 cookie에 넣으면 csrf 공격에 취약함. 그리고 이 코드는 그것도 고려하지 않았음...
  res.setHeader("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE");
  res.setHeader( // HTTP 헤더 허용 목록?
    "Access-Control-Allow-Headers",
    "X-Requested-With,content-type, Authorization"
  );
  next();
});

app.use("/", Router.mainRouter);
app.use("/user", Router.accountRouter);
app.use("/report", Router.adminRouter);
app.use("/manage", Router.manageRouter);

app.use(function (req, res, next) {
  var err = new Error("Page Not Found");
  err.status = 404;
  next(err);
});

if (app.get("env") === "development") {
  app.use(function (err, req, res, next) {
    res.status(err.status || 500);
    res.render("../pages/html/error.html"); 
  });
}

app.use(function (err, req, res, next) {
  res.status(err.status || 500);
});

server.listen(port, (err) => {
  if (err) {
    console.log(err);
  } else {
    loginSession.adminInit();
    adminReport.init();
    console.log(`server start success PORT : ${port}`);
  }
});
