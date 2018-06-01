
import os
import ssl
import asyncio
import uvloop
from sanic import Sanic
from sanic import response
from server.messagehub import handleMessage
from server.filehub import handleUpload
from server.filehub import handleDownload

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


app = Sanic()


@app.route('/', methods=['POST'])
async def handle_request(request):
    return response.json(handleMessage(request.json))

@app.route('/file/<apikey>', methods=['POST'])
async def handle_request(request, apikey):
    return response.json(handleUpload(request.body, apikey))

@app.route('/file/<apikey>/<filename>', methods=['GET'])
async def handle_request(request, apikey, filename):
    return await response.file(handleDownload(apikey))


if __name__ == '__main__':
    
    print(ssl.OPENSSL_VERSION)
    
    hostAddr = '0.0.0.0'

    certDir = ''

    #test if we are running on the server
    try:
        with open('is_server', 'r') as isServerFile:
            certDir = '/etc/letsencrypt/live/azenix.io/'
    except FileNotFoundError:
        print("not running on server")

    certPath = os.path.join(certDir, 'fullchain.pem')
    keyPath = os.path.join(certDir, 'privkey.pem')
    
    print("cert path: " + str(certPath))
    print("key path: " + str(keyPath))

    ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)
    # ctx.verify_mode = ssl.CERT_REQUIRED
    # ctx.load_verify_locations(os.path.join(CERT_DIR, 'CA.crt'))
    ctx.load_cert_chain(
        certfile=certPath,
        keyfile=keyPath
    )   
    app.run(host=hostAddr, port=443, ssl=ctx, workers=4)
