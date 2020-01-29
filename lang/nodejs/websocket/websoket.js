var http = require('http');
var WSServer = require('websocket').server;
var url = require('url');
var clientHtml = require('fs').readFileSync('client.html');
var plainHttpServer = http.createServer(function (req, res) {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(clientHtml);
}).listen(8080);
var webSocketServer = new WSServer({ httpServer: plainHttpServer });
var accept = ['test.com', '192.168.56.11'];
webSocketServer.on('request', function (req) {
    req.origin = req.origin || '*';
    if (accept.indexOf(url.parse(req.origin).hostname) === -1) {
        req.reject();
        console.log('Access from' + req.origin + 'is not permitted');
        return;
    }
    var websocket = req.accept(null, req.origin);
    websocket.on('message', function (msg) {
        console.log('receive' + '"' + msg.utf8Data + '"' + 'from' + req.origin);
        if (msg.utf8Data === 'Hello') {
            websocket.send('Hello! from Websocket server');
        }
    });
    websocket.on('close', function (code, desc) {
        console.log('disconnect:' + code + '-' + desc);
    });
});