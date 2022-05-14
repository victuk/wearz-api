const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const notes = new Schema({
    title: String,
    body: String,
    ownerId: UserSchema.Types.ObjectId,
    createDate: Date
});

const noteSchema = mongoose.model("notes", notes);
module.exports.noteSchema = noteSchema;
