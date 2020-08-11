from aiohttp import web
from aiohttp import WSMsgType
from aiohttp import ClientSession

platform = 'win64'
session = ClientSession()

async def index(request):
    return web.FileResponse('web/templates/list.html')


