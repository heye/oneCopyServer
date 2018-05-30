
import os
import ssl
import asyncio
import uvloop
from sanic import Sanic
from sanic import response
from server.messagehub import handleMessage

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


app = Sanic()


@app.route('/', methods=['POST'])
async def handle_request(request):
    return response.json(handleMessage(request.json))


if __name__ == '__main__':
    
    print(ssl.OPENSSL_VERSION)
    
    hostAddr = '0.0.0.0'

    ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLSv1_2)
    # ctx.verify_mode = ssl.CERT_REQUIRED
    # ctx.load_verify_locations(os.path.join(CERT_DIR, 'CA.crt'))
    ctx.load_cert_chain(
        certfile=os.path.join('fullchain.pem'),
        keyfile=os.path.join('privkey.pem')
    )   
    app.run(host=hostAddr, port=443, ssl=ctx, workers=4)
    netProxy.terminate()
