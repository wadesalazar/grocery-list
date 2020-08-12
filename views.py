from aiohttp import web
from aiohttp import WSMsgType
from aiohttp import ClientSession

import json

async def index(request):
    return web.FileResponse('web/templates/list.html')

async def update_list(request):

    data = await request.text()
    f = open("grocery-list.json",'wt')
    f.writelines(data)
    f.close
    #grocery_list = data

    return web.Response(text = "accepted")

async def get_list(request):
    grocery_list = open("grocery-list.json",'rt').read()
    return web.Response(body = grocery_list)