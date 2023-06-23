const mongoose = require('mongoose');
const { Schema } = mongoose;

const commentSchema = new Schema(
{
    title: {
        type: String,
        required: true,
    },
    description: {
        type: String,
        required: true,
    },
	user: {
        type: Schema.Types.ObjectId,
        ref: 'User',
        required: true,
    },
},
{
    timestamps: true
});

module.exports = mongoose.model('Comment', commentSchema);