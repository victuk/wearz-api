var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var cors = require('cors');
var mongoose = require('mongoose');
var jwt = require('jsonwebtoken');
var passport = require('passport');
var bodyParser = require('body-parser')
const passportJWT = require('passport-jwt');
const ExtractJwt = passportJWT.ExtractJwt;
var cloudinary = require('cloudinary').v2;
const JwtStrategy = passportJWT.Strategy;
const jwtOptions = {}
jwtOptions.jwtFromRequest = ExtractJwt.fromAuthHeaderWithScheme('jwt');
jwtOptions.secretOrKey = process.env.secretkey;

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');
var registerRouter = require('./routes/registeruser');
var loginRouter = require('./routes/login');
require('dotenv').config();
var app = express();


mongoose.connect(process.env.mongoConnection, { useNewUrlParser: true, useUnifiedTopology: true}, function(err) {
  if(err) {console.log(err)}
  else {console.log("Connected")}
});
// var db = mongoose.connection;
// db.once("open", callback => console.log("Connection Successful"));
// db.on("error", error => console.log(error));

cloudinary.config({
  cloud_name: 'dae4sosbl',
  api_key: '283128793578546',
  api_secret: '5n2fLu0S97IIA0u5acfTd56zwIg',
  secure: true
});

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(cors());
app.use(logger('dev'));
app.use(express.urlencoded({ extended: false }));
app.use(bodyParser.urlencoded({ extended: false }))

// parse application/json
app.use(bodyParser.json());
app.use(express.json());
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/v1/', indexRouter);
app.use('/v1/users', usersRouter);
app.use('/v1/register', registerRouter);
// app.use('/v1/registercompany', registerCompanyOwnerRouter);
// app.use('/v1/registerworkers', registerWorkersRouter);
app.use('/v1/login', loginRouter);


// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
