const jwt = require("jsonwebtoken");

const checkGroup = (req, value) => {
  let manager = /(manager[0-9]*)\w/g.test(value);
  // guest0manager01 우회 했당...😳
  if ((manager === true && !req.path.toLowerCase().includes("admin")) || value === "admin")
    return true;
  else return false;
};

module.exports = async function (req, res, next) {
  new Promise((resolve, reject) => {
    const JWT = req.cookies.JWT;
	console.log(req.cookies);
    if (JWT === null) {
      reject("JWT is null");
    } else {
      resolve(JWT);
    }
  })
    .then((token) => {
      jwt.verify(token, "[**SECRET_KEY**]", (err, result) => {
		console.log(result.id);
        if (err || result === null) {
          res.redirect("/");
        } else if (checkGroup(req, result.id) === true) {
          req.user_id = result.id;
          next();
        } else {
          res.redirect("/");
        }
      });
    })
    .catch((err) => {
      res.redirect("/");
    });
};
