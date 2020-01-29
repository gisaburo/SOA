var connect = require('connect');
var bodyParser = require('body-parser');
var util = require('util');
var form = require('fs').readFileSync('form.html');
var app = connect();
    app.use(bodyParser.urlencoded({extended: true}));
    app.use(function(req, res) {
        if (req.method === 'POST') {
            console.log('The user has posted the following data:\n' + util.inspect(req.body));
            res.end('Data you posted:\n' + util.inspect(req.body));
        }
        if (req.method === 'GET') {
            res.writeHead(200, {'Content-type': 'text/html'});
            res.end(form);
        }
    }).listen(8080);