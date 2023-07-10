const express=require('express');
const bodyParser=require('body-parser');
const ejs=require('ejs');
const hash=require('crypto-js/sha256');
const fs = require('fs');
const app=express();

var file={};
var read={};

function isObject(obj) {
  return obj !== null && typeof obj === 'object';
}

// setValue(file,filename,rename)
// a821c62e8104f8519d639b4c0948aece641b143f6601fa145993bb2e2c7299d4

function setValue(obj, key, value) {
  const keylist = key.split('.'); // 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824.flag
  const e = keylist.shift(); // shift가 python pop같은 존재임.
  if (keylist.length > 0) { // .을 이용해서 filename을 2개 보내면 되는거 아님??
    if (!isObject(obj[e])) obj[e] = {};
    setValue(obj[e], keylist.join('.'), value);
  } else {
    obj[key] = value;
	console.log(obj[key])
	console.log(Object.keys(obj))
    return obj;
  }
}

app.use(bodyParser.urlencoded({ extended: false })); // 이거를 적어야 실행이 되는게 있었는데....;;;; form 입력값 받으려면 입력해야 함.
app.set('view engine','ejs');

app.get('/',function(req,resp){
	read['filename']='fake'; // fake => flag
	resp.render(__dirname+"/ejs/index.ejs");
})

// b737ca7ee563ae80e457bb3d1dfe64edd2b4c015a8f88b6f87d5c113b68897fd

// 말 그대로 file만드는 곳임. 하지만  hash를 해서 만든다는 점...
app.post('/mkfile',function(req,resp){
	let {filename,content}=req.body;
	// let filename = req.body.filename;
	// let content = req.body.content;

	filename=hash(filename).toString(); // filename을 해쉬화 하는 이유는 보안을 위해서 임.
	// fs는 filesystem을 다루는 놈이다.
	fs.writeFile(__dirname+"/storage/"+filename,content,function(err){ // error가 있을 때만 err 파라미터에 값이 error값이 들어간다.
		if(err==null){
			file[filename]=filename;
			resp.send('your file name is '+filename);
		}else{
			resp.write("<script>alert('error')</script>");
			resp.write("<script>window.location='/'</script>");
		}
	})
})

// file.__proto__.2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

// {"__proto__":{"status":"polluted"}}

app.get('/readfile',function(req,resp){
	console.log(req.query.filename);
	let filename=file[req.query.filename];
	console.log(filename);
	// 아까 만든 filename을 넣으면 filename의 value의 값도 filename이기 때문에 그냥 filename이 가져와짐.

	if(filename==null){ // 만약 아무 filename도 없다면 error 결국에는 여기만 .그걸 검사안하기 때문에 이걸로 들어가야 함. 어떻게???
		fs.readFile(__dirname+'/storage/'+read['filename'],'UTF-8',function(err,data){
			resp.send(data);
		})
	}else{ // 정상적으로 입력이 되었다면....!
		read[filename]=filename.replaceAll('.',''); // 굳이 filename에서 .을 없에야 했나....??? 어차피 hash인데???
		console.log(Object.keys(read))
		fs.readFile(__dirname+'/storage/'+read[filename],'UTF-8',function(err,data){
			// data에는 filename 내용이 들어간다 어떻게??? fs.readFile 마지막에 callback 함수가 있기 때문이다. 앞에 다 실행이 되고 난후 callback 함수가 실행이 되어서 file의 error와 data를 가질 수 있는거다.
			// JavaScript에서 콜백(callback) 함수란, 다른 함수의 인자로 전달되어 특정 함수가 수행한 작업이 완료되었음을 알리는 역할을 하는 함수를 의미합니다. 
			
			if(err==null){
				resp.send(data);
			}else{
				resp.send('file is not existed');
			}
		})
	}
})

// /test?func=rename&filename={}.__proto__.filename&rename=flag

// /test?func=rename&filename=__proto__.filename&rename=%2e%2e/%2e%2e/flag
// /test?func=rename&filename=read.__proto__.filename&rename=%2e%2e/%2e%2e/flag

// /test?func=rename&filename=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824.__proto__.filename&rename=%2e%2e/%2e%2e/flag

// /test?func=rename&filename=read.filename&rename=../../flag
// /test?func=rename&filename=2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824&rename=__proto__

app.get('/test',function(req,resp){
	let {func,filename,rename}=req.query;
	if(func==null){
		resp.send("this page hasn't been made yet");
	}else if(func=='rename'){
		setValue(file,filename,rename)
		// console.log(file['2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824']);
		resp.send('rename');
	}else if(func=='reset'){
		read={};
		resp.send("file reset");
	}
})

app.listen(8000);

// 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

