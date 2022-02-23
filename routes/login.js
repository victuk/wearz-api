var express = require('express');
var router = express.Router();
var regUser = require('../models/register');
require('dotenv').config();
const passportJWT = require('passport-jwt');
const jwt = require('jsonwebtoken');
const ExtractJwt = passportJWT.ExtractJwt;
const jwtOptions = {};
jwtOptions.jwtFromRequest = ExtractJwt.fromAuthHeaderWithScheme('jwt');
jwtOptions.secretOrKey = process.env.secretkey;

router.post('/', (req, res) => {
    if (req.body.email && req.body.password) {
        const email = req.body.email;
        const password = req.body.password;
        regUser.getUserByEmail(email, (err, user) => {
            if (!user) {
                res.json({ status: false, message: 'The user does not exist!' });
            } else {
                regUser.comparePassword(password, user.password, (error, isMatch) => {
                    if (error) throw error;
                    if (isMatch) {
                        if (user.role == 'user' || user.role == 'admin') {
                            const payload = { id: user.id, role: user.role};
                            const token = jwt.sign(payload, jwtOptions.secretOrKey);
                            res.json({ status: true, token, email: user.email, role: user.role });
                        }

                    } else {
                        res.status(401).json({
                            status: false,
                            message: 'The password is incorrect!'
                        });
                    }
                });
            }
        });
    } else {
        res.json({status: false, message: 'You need to input a valid username and password.'});
    }
});

module.exports = router;
