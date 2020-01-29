var http = require('http');
var path = require('path');
var fs = require('fs');
var mimeTypes = {
    '.js': 'text/javascript',
    '.html': 'text/html',
    '.css': 'text/css'
};
var cache = {};
http.createServer(function (request, response) {
    var lookup = path.basename(decodeURI(request.url)) || 'index.html',
    f = 'content/' + lookup;
    fs.exists(f, function (exists) {
        if (exists) {
            var headers = {'Content-type': mimeTypes[path.extname(f)]};
                if (cache[f]) {
                    response.writeHead(200, headers);
                    response.end(cache[f].content);
                    return;
                }
                var s = fs.createReadStream(f).on('open', function() {
                    response.writeHead(200, headers);
                    this.pipe(response);
                }).once('error', function (e) {
                    console.log(e);
                    response.writeHead(500);
                    response.end('サーバーエラー！');
                });
        }
        response.writeHead(404, {'Content-Type': 'text/html; charset=utf-8'});
        response.end('ページが見つかりません！');
    });
}).listen(8080);