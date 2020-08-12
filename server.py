from aiohttp import web
from routes import setup_routes

app = web.Application()

app['list'] = {}

setup_routes(app)

web.run_app(app, port="8081")