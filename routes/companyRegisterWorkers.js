var express = require('express');
var router = express.Router();
var regUser = require('../models/register');


router.post('/reg-staff', function (req, res) {
    if (req.body.email &&
        req.body.password &&
        req.body.role &&
        req.body.firstName &&
        req.body.lastName &&
        req.body.phoneNumber &&
        req.body.gender &&
        req.body.location &&
        req.body.companyDetails &&
        req.body.managerDetails) {

    const firstName = req.body.firstName;
    const lastName = req.body.lastName;
    const gender = req.body.gender;
    const email = req.body.email;
    const phoneNumber = req.body.phoneNumber;
    const password = req.body.password;
    const role = req.body.role;
    const location = req.body.location;
    const companyDetails = req.body.companyDetails;
    const managerDetails = req.body.managerDetails;

    const newUser = new regUser({
        firstName,
        lastName,
        gender,
        email,
        phoneNumber,
        password,
        role,
        location,
        status: 'active',
        companyDetails,
        managerDetails
    });

    regUser.getUserByEmail(email, (err, user) => {
        if (!user) {
            regUser.createUser(newUser, function (error, user) {
                if (error) {
                    res.status(422).json({
                        message: 'Something went wrong!'
                    })
                }
                res.json({ message: 'ok', user });
            });
        } else {
            res.json({message: "This email is already used"});
        }
    });


} else {
    res.json({message: 'Your input details are not complete.'});
}

});


router.post('/reg-driver', function (req, res) {
    if (req.body.email &&
        req.body.firstName &&
        req.body.lastName &&
        req.body.gender &&
        req.body.password &&
        req.body.role &&
        req.body.location &&
        req.body.plateNumber &&
        req.body.companyDetails &&
        req.body.managerDetails) {

    const firstName = req.body.firstName;
    const lastName = req.body.lastName;
    const gender = req.body.gender;
    const email = req.body.email;
    const plateNumber = req.body.plateNumber;
    const password = req.body.password;
    const role = req.body.role;
    const location = req.body.location;
    const companyDetails = req.body.companyDetails;
    const managerDetails = req.body.managerDetails;

    const newUser = new regUser({
        firstName,
        lastName,
        gender,
        email,
        plateNumber,
        password,
        role,
        location,
        status: 'active',
        companyDetails,
        managerDetails
    });

    regUser.getUserByEmail(email, (err, user) => {
        if (!user) {
            regUser.createUser(newUser, function (error, user) {
                if (error) {
                    res.status(422).json({
                        message: 'Something went wrong!'
                    })
                }
                res.json({ message: 'ok', user });
            });
        } else {
            res.json({message: "This email is already used"});
        }
    });


} else {
    res.json({message: 'Your input details are not complete.'});
}

});

router.post('/reg-manager-admin', function (req, res) {
    if (req.body.email &&
        req.body.firstName &&
        req.body.lastName &&
        req.body.gender &&
        req.body.password &&
        req.body.role &&
        req.body.location &&
        req.body.companyDetails) {

    const firstName = req.body.firstName;
    const lastName = req.body.lastName;
    const gender = req.body.gender;
    const email = req.body.email;
    const password = req.body.password;
    const role = req.body.role;
    const location = req.body.location;
    const companyDetails = req.body.companyDetails;
    const officeAddress = req.body.officeAddress;

    const newUser = new regUser({
        firstName,
        lastName,
        gender,
        email,
        password,
        role,
        location,
        companyDetails,
        createDate: Date.now()
    });

    regUser.getUserByEmail(email, (err, user) => {
        if (!user) {
            regUser.createUser(newUser, function (error, user) {
                if (error) {
                    res.status(422).json({
                        message: 'Something went wrong!'
                    })
                }
                res.json({ message: 'ok', user });
            });
        } else {
            res.json({message: "This email is already used"});
        }
    });


} else {
    res.json({message: 'Your input details are not complete.'});
}

});

module.exports = router;
