var express = require('express');
var router = express.Router();
const { order } = require('../models/orders');
const authLogin = require("../auth/loginAuth");

router.get('/orders', authLogin, async function(req, res) {
    const orders = await order.find().populate("ownerId");
    res.json({
        successful: true,
        orders
    });
});

router.get('/order/:orderId', authLogin, async function(req, res) {
    const {orderId} = req.params;
    const orders = await order.findById(orderId).populate("ownerId");
    res.json({
        successful: true,
        orders
    });
});

router.post('/order', authLogin, function(req, res) {
    
    let {path, amount, paystackPaymentDetails} = req.body;
    let {id: ownerId} = req.decoded;
    
    const newOrder = new order({
        pathToClothe: path,
        amount,
        ownerId,
        paystackPaymentDetails,
        orderStatus: 'pending',
        createDate: Date.now(),
        modifyDate: Date.now()
    });



    newOrder.save(function(err, newSavedOrder) {
        if (err) console.log(err);
        res.json({
            successful: true,
            newSavedOrder
        });
    });
});

router.patch('/order', async function(req, res) {
    const {orderID, orderStatus} = req.body;
    const updatedOrder = await order.findByIdAndUpdate(orderID, {
        orderStatus
    }, {new: true});



    res.json({
        successful: true,
        updatedOrder
    });
});

router.delete('/order', function(req, res) {
    const { orderID } = req.body;
    order.findByIdAndDelete(orderID, function(err, deletedUser) {
        if(err) console.log(err);
        res.json({
            successful: true
        });
    });
});

module.exports = router;