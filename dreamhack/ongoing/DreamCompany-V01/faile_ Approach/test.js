// const crypto = require('crypto');

// const encoding = (input) => {
// 	return crypto.createHash("sha256").update(input).digest("hex");
// };

// password = encoding("shs2848divv8ru4uwau3u48sdifjsigjirjgls8bvcawe115331497");

// // console.log(password);

// setTimeout(() => {
//     console.log(password);
//   }, 1000);

// const result = encoding("admin");

// // console.log(result);

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
//  const report_list = {};
//   const reportInit = () => {
// 	const report_msg = [
// 	  "[**SECRET_CONTENT**]",
// 	  "[**SECRET_CONTENT**]",
// 	  "[**SECRET_CONTENT**]",
// 	  "[**SECRET_CONTENT**]",
// 	  "[**SECRET_CONTENT**]",
// 	  "[**SECRET_CONTENT**]",
// 	  "[**SECRET_CONTENT**]",
// 	];
// 	for (let i = 0; i < report_msg.length; i++) {
// 	  report_list[i] = {
// 		id: i,
// 		type: "report",
// 		group: i < 3 ? "admin" : "super_admin",
// 		msg: report_msg[i],
// 		time: new Date().getTime(),
// 	  };
// 	}
//   };

// const password = reportInit();

// console.log(password);

// const printAllTimeStrings = () => {
//     for (let i = 0; i < 86400000; i++) {
// 		if (password == i) {
// 			console.log("Solve");
// 			break;
// 		}
//         console.log(i);
//     }
// };

// // printAllTimeStrings();


// const jwt = require("jsonwebtoken");

// createAccessToken = function (user_id) {
//   return (accessToken = jwt.sign(
//     {
//       id: user_id,
//     },
//     "[**SECRET_KEY**]",
//     {
//       expiresIn: "1h",
//       issuer: "cotak",
//     }
//   ));
// };

// const settingJWT = () => {
// 	const AccessToken = createAccessToken("admin");
// 	console.log(AccessToken);
// 	if (AccessToken) {
// 	  console.log("Access");
// 	} else {
// 	  console.log("Failed");
// 	}
//   };
const time = getTime();
console.log(time);
// //   settingJWT();