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
	if (this.isModified("password")) { // 여기서 this는 userSchema의 그러니깐 User 생성자의 인스턴스를 말한다.
	  this.password = await bcrypt.hash(this.password, 5);
	}
  });

module.exports = mongoose.model('User', userSchema); // <- 여기서 User로 include할 수 있게 만들어줘서 위에서 User 생성자라고 설명한 거임.