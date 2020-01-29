var http = require('http');
var querystring = require('querystring');
var util = require('util');
var form = require('fs').readFileSync('form.html');
var maxData = 2 * 1024 * 1024;

http.createServer(function (req, res) {
    if (req.method === 'GET') {
        res.writeHead(200, {'Content-Type': 'text/html; charset=utf8'});
        res.end(form);
    }
    if (req.method === 'POST') {
        var postData = '';
        req.on('data', function (chunk) {
            postData += chunk;
            if (postData.length > maxData) {
                postData = '';
                this.pause();
                res.writeHead(443);
                res.end('Post data too large');
            }
        }).on('end', function() {
            if (!postData) { res.end(); return; }
            var postDataObject = querystring.parse(postData);
            console.log('The user has posted the following data:\n' + postData);
            res.end('Data you posted:\n' + util.inspect(postDataObject));
        });
    }
}).listen(8080);