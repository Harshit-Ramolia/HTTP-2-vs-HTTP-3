## Express server (HTTP/1.1)
To run the HTTP/1.1 server, execute the following in  a terminal:
```
node Express/myserver.js
```

## HTTP/2 server
To run the HTTP/2 server, execute the following in  a terminal:
```
node HTTP2/server.js
```

## HTTP/3 server
Running the HTTP/3 server requires installing the [`aioquic` library](https://github.com/aiortc/aioquic).

After installation, please run the following commands from the root directory in separate terminals to access the server:

```
python HTTP3/http3_server.py --certificate HTTP3/ssl_cert.pem --private-key HTTP3/ssl_key.pem
```

```
google-chrome \
  --enable-experimental-web-platform-features \
  --ignore-certificate-errors-spki-list=BSQJ0jkQ7wwhR7KvPZ+DSNk2XTZ/MS6xCbo9qu++VdQ= \
  --origin-to-force-quic-on=localhost:4433 \
  https://localhost:4433/
```

