# HTTP/3 server

## Installation
Please refer this https://github.com/aiortc/aioquic/tree/main/examples to install aioquic library, which is needed to run HTTP/3 server

## Running
Run following commands from root directory in seperate terminals to access the server
`
python HTTP3/http3_server.py --certificate HTTP3/ssl_cert.pem --private-key HTTP3/ssl_key.pem
`

`
google-chrome \
  --enable-experimental-web-platform-features \
  --ignore-certificate-errors-spki-list=BSQJ0jkQ7wwhR7KvPZ+DSNk2XTZ/MS6xCbo9qu++VdQ= \
  --origin-to-force-quic-on=localhost:4433 \
  https://localhost:4433/
`