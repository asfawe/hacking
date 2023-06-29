function base64(json) {
    const stringified = JSON.stringify(json)
    // JSON을 문자열화
    const base64Encoded = Buffer.from(stringified).toString("base64")
    // 문자열화 된 JSON 을 Base64 로 인코딩
    const paddingRemoved = base64Encoded.replaceAll("=", "")
    // Base 64 의 Padding(= or ==) 을 제거
  
    return paddingRemoved
  }
 

const payload = {
	id: "guest",
	  iat: 1687928577,
	  exp: 1687932177,
	  iss: "cotak"
  }

const encodedPayload = base64(payload)

const tmp_jwttoken = `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.${encodedPayload}.0bo5DoblnwcXczHCnSkUtiE0scW255K5CoD-XqeJJAc`

console.log(tmp_jwttoken)