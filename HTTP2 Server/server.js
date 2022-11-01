const http2 = require('node:http2');
const fs = require('node:fs');

const server = http2.createSecureServer({
  key: fs.readFileSync('HTTP2 Server\localhost-cert.pem'),
  cert: fs.readFileSync('HTTP2 Server\localhost-cert.pem')
});
server.on('error', (err) => console.error(err));

