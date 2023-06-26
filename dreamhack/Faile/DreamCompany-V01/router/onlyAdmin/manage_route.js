const express = require("express");
const path = require("path");
const router = express.Router();
const checkToken = require("../../apis/token/checkToken");
const session = require("../../apis/session/session");

router.use(express.static("../pages/css"));
router.use(express.static("../pages/js"));

router.get("/", checkToken, function (req, res, next) {
  res.sendFile(
    path.join(__dirname, "..", "..", "..", "/pages/html/manage.html")
  );
});

// 으흠...!! 그러면 만약 이걸 우회하면 모든 session을 json 형태로 볼 수 있기 때문에 admin도 볼 수 있겠네??
router.get("/session", checkToken, function (req, res, next) {
  const all_session = session.all_session;
  res
    .json({
      session: all_session,
    })
    .status(200);
});

router.post("/", function (req, res, next) {});

module.exports = router;
