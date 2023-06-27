const crypto = require('crypto');

const encoding = (input) => {
	return crypto.createHash("sha256").update(input).digest("hex");
};

const result = encoding("admin");

console.log(result);

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

const password = getTime();

const printAllTimeStrings = () => {
    for (let i = 0; i < 86400000; i++) {
		if (password == i) {
			console.log("Solve");
			break;
		}
        console.log(i);
    }
};

// printAllTimeStrings();


const jwt = require("jsonwebtoken");

createAccessToken = function (user_id) {
  return (accessToken = jwt.sign(
    {
      id: user_id,
    },
    "[**SECRET_KEY**]",
    {
      expiresIn: "1h",
      issuer: "cotak",
    }
  ));
};

const settingJWT = () => {
	const AccessToken = createAccessToken("admin");
	console.log(AccessToken);
	if (AccessToken) {
	  console.log("Access");
	} else {
	  console.log("Failed");
	}
  };

  settingJWT();