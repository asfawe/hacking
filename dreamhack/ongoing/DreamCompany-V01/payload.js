const crypto = require("crypto")

function base64(json) {
    const stringified = JSON.stringify(json)
    // JSON을 문자열화
    const base64Encoded = Buffer.from(stringified).toString("base64")
    // 문자열화 된 JSON 을 Base64 로 인코딩
    const paddingRemoved = base64Encoded.replaceAll("=", "")
    // Base 64 의 Padding(= or ==) 을 제거
  
    return paddingRemoved
  }
 
  const header = {
    alg: "HS256",
    typ: "JWT",
  }
  
  const encodedHeader = base64(header)
  // console.log(encodedHeader)
 
  const payload = {
    id: "admin",
  	iat: 1687864147,
  	exp: 1687867747,
  	iss: "cotak"
  }
  
  const encodedPayload = base64(payload)
//   console.log(encodedPayload)

  const tmp_jwttoken = `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.${encodedPayload}.-OM0vS9kQ9XXHaz7CpxG3A9RtR8yle5jaFvC8pdleUU`
  console.log(tmp_jwttoken);
// 요청 부분

  const axios = require('axios');
  const jwtToken = tmp_jwttoken;

//   const data = {
// 	username: 'username',
// 	password: 'password'
//   };
  
  axios.get('http://host3.dreamhack.games:21064/', {
	headers: {
	  Authorization: `Bearer ${jwtToken}`
	}
  })
  .then(response => {
	console.log(response.data);
  })
  .catch(error => {
	console.error(error);
  });