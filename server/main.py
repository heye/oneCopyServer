
import os
import ssl
import asyncio
import uvloop
from sanic import Sanic
from sanic import response
from messagehub import handleMessage
from filehub import handleUpload
from filehub import handleDownload

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

    app.run(host=hostAddr, port=4444, workers=4)
