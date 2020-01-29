var http = require('http');
var url = require('url');
var profiles = require('./profiles');
http.createServer(function (req, res) {
    var urlObj = url.parse(req.url, true);
    var cb = urlObj.query.callback;
    var who = urlObj.query.who;
    var profile;
    if (cb && who) {
        profile = cb + "(" + JSON.stringify(profiles[who]) + ")";
        res.end(profile);
    }
}).listen(8080);