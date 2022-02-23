const jwt = require('jsonwebtoken');
const User = require('../models/register');
const jwtOptions = {};
require('dotenv').config();
jwtOptions.secretOrKey = process.env.secretkey;

function authLogin(req, res, next){
    const token = req.body.token || req.headers.token;
    if(token){
        jwt.verify(token, jwtOptions.secretOrKey, function(err, decoded){
            if(err){
                return res.json({ success: false, message: 'Failed to authenticate token.' });
            } else {
                req.decoded = decoded;
                User.findById(req.decoded.id, 'status', (err, user) => {
                    
                    if (err) {
                        return console.log(err);
                    }
                    
                    if (user) {
                        next()
                        
                    } else {
                        res.json({status: 'User does not exist'})
                    }

                });
            }
        })
    } else {
        res.json({status: 'notLoggedIn', message:'You will need to login'});
    }
}

module.exports = authLogin;
