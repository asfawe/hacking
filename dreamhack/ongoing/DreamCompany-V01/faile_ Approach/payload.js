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
  
//   const encodedHeader = base64(header)
  // console.log(encodedHeader)
 
const hehe = async () => {
	for (let i = 1687917048; i < 1687920648; i++) {

		// const payload = {
		//   	id: "admin",
		// 	iat: i,
		// 	exp: i+3600,
		// 	iss: "cotak"	
		// }
		const payload = {
			id: "guest",
			  iat: 1687928577,
			  exp: 1687932177,
			  iss: "cotak"
		  }
		
		const encodedPayload = base64(payload)
	  //   console.log(encodedPayload)
	  
		let tmp_jwttoken = `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.${encodedPayload}.0bo5DoblnwcXczHCnSkUtiE0scW255K5CoD-XqeJJAc`
		
		tmp_jwttoken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Imd1ZXN0IiwiaWF0IjoxNjg3OTI5ODY0LCJleHAiOjE2ODc5MzM0NjQsImlzcyI6ImNvdGFrIn0.NADNuXN9pIBzDN_sbglSWE8giJolJIFVNXit4s8zM4A"
	  
	  // 요청 부분
	  
		const axios = require('axios');
	  
		await axios.get('http://localhost:8000/session', {
			headers: {
				'Content-Type': 'application/json'
			},
			// 쿠키를 설정
			cookies: {
				"JWT" : "haha",
				JWT: tmp_jwttoken
			}
		})
		.then(response => {
			console.log(response.cookies);
		  if (response.config.data) {
			console.log("hahahahha")
			console.log(i)
			console.log(payload)
		  }
		})
		.catch(error => {
		  console.error(error);
		});
		console.log(i);
	  }
} 

hehe();