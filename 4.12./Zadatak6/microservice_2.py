from aiohttp import web 
import asyncio

async def handler_function(request):
    await asyncio.sleep(4)
    return web.json_response({"message": "Pozdrav nakon 4 sekunde"}, status = 200)

app = web.Application()

app.router.add_get("/pozdrav", handler_function)

web.run_app(app, port=8082)
