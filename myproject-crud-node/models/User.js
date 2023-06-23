const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const { Schema } = mongoose;

const userSchema = new Schema(
{
	email: {
		type: String,
		required: true,
	},
	username:String,
	password: {
		type: String,
		required: true,
	},
},
{
	timestamps: true
});

userSchema.pre("save", async function () {
	if (this.isModified("password")) { // 만약 비밀번호가 변경되었다면 (예를 들어, 처음 생성되었거나 사용자가 비밀번호를 업데이트한 경우), 이 미들웨어는 bcrypt를 사용하여 비밀번호를 해싱합니다.
	  this.password = await bcrypt.hash(this.password, 5); // 이 경우 this는 userSchema에 따라 생성된 문서, 즉 하나의 'User'를 가리킵니다. 
	}
  });

module.exports = mongoose.model('User', userSchema); // <- 여기서 User로 include할 수 있게 만들어줘서 위에서 User 생성자라고 설명한 거임.