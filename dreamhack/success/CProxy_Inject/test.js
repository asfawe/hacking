// const dns = require('dns/promises');

// function isPrivateIP(ip) {
//     var s = ip.split('.').map(x => parseInt(x, 10));
//     return s[0] === 10 ||                               // 10.0.0.0/8
//         (s[0] === 172 && s[1] >= 16 && s[1] < 32) ||    // 172.16.0.0/12
//         (s[0] === 192 && s[1] === 168) ||               // 192.168.0.0/16
//         s[0] === 127 ||                                 // 127.0.0.0/8
//         ip === '0.0.0.0';                               // 0.0.0.0/32
// }

// async function isSafeHost(host) {
//     if (!/^[A-Za-z0-9.]+$/.test(host)) {
//         return false;
//     }
//     try {
//         const address = await dns.resolve4(host);
// 		console.log(address);
// 		console.log(address.every(addr => !isPrivateIP(addr)));
//         return address.every(addr => !isPrivateIP(addr));
//     } catch {
//         return false;
//     }
// }

// isSafeHost('localhost');

const rid = parseInt("hehehe", 10);

console.log(rid);