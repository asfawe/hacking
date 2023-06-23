const mongoose = require('mongoose');
const { Schema } = mongoose;

const userSchema = new Schema(
{
	email: {
		type: String,
		required: true,
	},
	name:String,
	age:{
		type: Number,
		min: 10,
		max: 50,
	}
},
{
	timestamps: true
});

module.exports = mongoose.model('User', userSchema);