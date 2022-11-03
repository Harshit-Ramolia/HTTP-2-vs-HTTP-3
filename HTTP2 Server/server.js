// file: ./server.js

const http2 = require('http2')

// // create a new server instance
// const server = http2.createServer()

const fs = require('fs')

const server = http2.createSecureServer({
  // we can read the certificate and private key from
  // our project directory
  key: fs.readFileSync('key.pem'),
  cert: fs.readFileSync('cert.pem')
})

function push (stream, filePath) {
  const { file, headers } = getFile(filePath)
  const pushHeaders = { [HTTP2_HEADER_PATH]: filePath }

  stream.pushStream(pushHeaders, (pushStream) => {
    pushStream.respondWithFD(file, headers)
  })
}


// log any error that occurs when running the server
server.on('error', (err) => console.error(err))

// the 'stream' callback is called when a new
// stream is created. Or in other words, every time a
// new request is received
server.on('stream', (stream, headers) => {
  // we can use the `respond` method to send
  // any headers. Here, we send the status pseudo header
  console.log( headers[':path'])
  if ( headers[':path'] == "/"){
    stream.respond({
          ':status': 200
    })
    // stream.end('Hello World')
    // push(res.stream, 'bundle1.js')
  }else{
    stream.respond({
      ':status': 200
    })
    stream.end()
  }
})

// const router = require('./router')``
// server.on('stream', router)

// start the server on port 8000
server.listen(8000, () => {
  console.log("App is running at port 8000");
})
