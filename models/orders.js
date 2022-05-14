const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const User = require('./register');
const UserSchema = mongoose.model('User', User.User);

const orderSchema = new Schema({
    pathToClothe: String,
    amount: String,
    ownerId: { type: Schema.Types.ObjectId, ref: UserSchema },
    orderStatus: String,
    paystackPaymentDetails: Object,
    createDate: Date,
    updateDate: Date
});

const order = mongoose.model("orders", orderSchema);
module.exports.order = order;