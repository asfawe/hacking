const express = require("express"); // Express.js는 웹 애플리케이션을 만드는 데 매우 인기 있는 Node.js 프레임워크입니다.
const session = require("express-session"); // 이 미들웨어는 세션을 관리하는데 사용됩니다.
const logger = require("morgan"); // Morgan은 HTTP 요청 로거 미들웨어로, 서버에 들어오는 요청을 로깅하는데 사용됩니다.
const cookieParser = require("cookie-parser"); // 이 미들웨어는 쿠키를 파싱하여 req.cookies 객체로 만들어주는 역할을 합니다.
const loginSession = require("./apis/session/session");
const adminReport = require("./apis/admin/admin_report");
const Router = require("./router/index/index_route");
const port = process.env.PORT || 8000; // 서버가 사용할 포트를 설정합니다. 환경 변수 PORT가 설정되어 있다면 그 값을 사용하고, 그렇지 않으면 기본값으로 8000을 사용합니다.
const app = express(); // Express 애플리케이션 인스턴스를 생성하여 app 변수에 할당합니다.
const server = require("http").createServer(app); // Node.js의 기본 HTTP 모듈을 사용하여 새 HTTP 서버를 생성하고 쉽게 말하면 http로 요청이 들어왔을 때 응답을 해줄 얘를 만들어 주고, 이를 server 변수에 할당합니다.

const options = {
	swaggerDefinition: {
	  openapi: "3.0.0",
	  info: {
		title: "TheCodebuzz API",
		version: "1.0.0"
	  },
	  servers: [
		{
		  url: "http://localhost:8000/"
		}
	  ]
	},
	apis: ["./router/**/*.js"]
  };

const swaggerUi = require("swagger-ui-express");

const swaggerJsondoc = require("swagger-jsdoc");

const specs = swaggerJsondoc(options);
app.use("/docs", swaggerUi.serve);


app.use("/docs", swaggerUi.serve, swaggerUi.setup(specs, { explorer: true }));


app.use(logger("dev"));	// 서버로 들어오는 http 요청에 대한 로그를 생성할 건데 dev 포맷으로 하겠다. dev 포맷은 말 그대로 개발 환경에서 유용한 형식으로 로그를 출력한다.
app.use(express.json()); // 클라이언트가 JSON 형식의 데이터를 보내면, 이 미들웨어는 그 데이터를 JavaScript 객체로 변환하고 req.body에 저장합니다.
app.use(express.urlencoded({ extended: true })); // 이 형식은 일반적으로 HTML 폼에서 전송됩니다. extended: true 옵션은 복잡한 객체나 배열을 인코딩하는 데 사용됩니다.
app.use(cookieParser("[**SECRET_KEY**]")); // 이 미들웨어는 요청 헤더의 쿠키를 파싱하여 req.cookies 객체로 만들어줍니다.
app.use(
  session({
    resave: false, // 세션이 수정되지 않아도 매번 저장소에 저장할지 여부를 설정합니다.
    saveUninitialize: true, // 초기화되지 않은 세션까지 db나 저장소에 저장한다는 거임. 초기화 되지 않았다는 뜻은 서버에서 새로운 세션 객체를 생성했으나 아직 사용자 특정 데이터나 값이 할당되지 않은 상태를 말합니다
    secret: "[**SECRET_KEY**]", // 쿠키의 서명은 클라이언트 측에서 쿠키가 변경되지 않았음을 보증하는 방법입니다. 다시 말하면 cookie를 변경할 때 무조건 secret_key가 필요하다는 거임. 
    cookie: {
      httpOnly: true, // 클라이언트 측 스크립트를 통해 쿠키에 접근하는 것을 방지하고, 
      secure: false, //  HTTPS를 사용하지 않는 경우에도 쿠키를 전송하도록 설정합니다.
    },
    name: "cookie", // 세션 쿠키의 이름을 설정합니다.
  })
);

app.use(function (req, res, next) {
  res.setHeader("Access-Control-Allow-Origin", "self");
  res.setHeader("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE");
  res.setHeader(
    "Access-Control-Allow-Headers", // 요청 헤더 중 어떤 것들이 교차 출처 요청에서 허용되는지를 지정합니다.
    "X-Requested-With,content-type, Authorization" // 여기서는 X-Requested-With, content-type, Authorization 헤더가 허용됩니다.
	/* 이 코드에서는 X-Requested-With, content-type, Authorization 이라는 세 가지 HTTP 헤더를 허용하고 있습니다:

X-Requested-With: 일반적으로 AJAX 요청을 식별하는 데 사용됩니다. 예를 들어, JavaScript에서 XMLHttpRequest 객체를 사용하여 요청을 생성할 때 이 헤더가 추가될 수 있습니다.

content-type: 요청 본문의 미디어 유형을 지정하는 데 사용됩니다. 예를 들어, 클라이언트가 JSON 데이터를 전송하는 경우, content-type 헤더는 application/json으로 설정됩니다.

Authorization: 클라이언트가 서버에게 인증 정보(예: 토큰, 사용자 이름 및 비밀번호)를 제공하는 데 사용됩니다. 이 헤더를 사용하여 클라이언트가 자신을 식별하고, 서버는 이 정보를 기반으로 접근 권한을 부여합니다. */
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