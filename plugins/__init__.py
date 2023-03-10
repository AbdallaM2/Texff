from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Mᴋɴ Bᴏᴛᴢ")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app


__repo__ = "https://github.com/AbdallaM01/autofilter.extra"
__license__ = "GNU GENERAL PUBLIC LICENSE V2"
__copyright__ = "Copyright (C) 2023-present Abdalla <https://github.com/AbdallaM01>"
