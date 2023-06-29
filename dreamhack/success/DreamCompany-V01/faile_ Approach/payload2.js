const crypto = require("crypto")
const axios = require('axios');
const axiosCookieJarSupport = require('axios-cookiejar-support');
const tough = require('tough-cookie');

axiosCookieJarSupport(axios);

const cookieJar = new tough.CookieJar();

function base64(json) {
    const stringified = JSON.stringify(json)
    const base64Encoded = Buffer.from(stringified).toString("base64")
    const paddingRemoved = base64Encoded.replaceAll("=", "")
  
    return paddingRemoved
}

const header = {
    alg: "HS256",
    typ: "JWT",
}

const hehe = async () => {
    for (let i = 1687917048; i < 1687920648; i++) {

        const payload = {
            id: "guest",
            iat: 1687928577,
            exp: 1687932177,
            iss: "cotak"
        }
        
        const encodedPayload = base64(payload)
        let tmp_jwttoken = `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.${encodedPayload}.0bo5DoblnwcXczHCnSkUtiE0scW255K5CoD-XqeJJAc`
        
        tmp_jwttoken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Imd1ZXN0IiwiaWF0IjoxNjg3OTI5ODY0LCJleHAiOjE2ODc5MzM0NjQsImlzcyI6ImNvdGFrIn0.NADNuXN9pIBzDN_sbglSWE8giJolJIFVNXit4s8zM4A"

        try {
            const response = await axios.get('http://localhost:8000/session', {
                headers: {
                    'Content-Type': 'application/json'
                },
                jar: cookieJar, // tough.CookieJar or boolean
                withCredentials: true, // If true, send cookie stored in jar
                cookies: {
                    "JWT" : "haha",
                    JWT: tmp_jwttoken
                }
            });

            console.log(response.cookies);

            if (response.config.data) {
                console.log("hahahahha")
                console.log(i)
                console.log(payload)
            }
        } catch (error) {
            console.error(error);
        }

        console.log(i);
    }
}

hehe();