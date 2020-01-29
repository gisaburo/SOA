// server infomation
var hostname = '192.168.56.11';
var port = 8080;

// require
var http = require('http');
var path = require('path');
var fs = require('fs');
//var contentDisposition = require('content-disposition');

// mimeTypes
var mimeTypes={
    '.html' : 'text/html',
//    '.css' : 'text/css',
    '.js' : 'text/javascript',
//    '.jpg' : 'image/jpg',
//    '.png' : 'image/png',
//    '.mp3' : 'audio/mpeg'
    '.txt' : 'text/plain'
};

//var filePath = "http://192.168.56.11:8080/content/aaa.txt"

// create server
http.createServer(function (request, response) {
    var lookup = path.basename(decodeURI(request.url)) || 'index.html',
    f = 'content/' + lookup;
    fs.exists(f, function (exists) {
        if (exists) {
            fs.readFile(f, function (err, data) {
                if (err) {
                    response.writeHead(500);
                    response.end('Server Error!');
                    return;
                }
                var headers = {'Content-Type': mimeTypes[path.extname(f)]};
                //var headers = ('Content-Disposition', contentDisposition(filePath))
                response.writeHead(200, headers);
                response.end(data);
            });
            return;
        }
        response.writeHead(404, {'Content-Type': 'text/html; charset=utf-8'});
        response.end('page not found.');
    });
}).listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
