from aiohttp import web 
from functools import reduce

async def handler_function(request):
    request_data = await request.json()
    
    if type(request_data) != list:
        return web.json_response({"Odgovor": "Nije proslijedena lista"}, status = 400)

    for x in request_data:
        if type(x) != int and type(x) != float:
            return web.json_response({"Odgovor": "U listi nisu proslijedeni brojevi"}, status = 400)

    sum = reduce(lambda x, y: x + y, request_data)

    return web.json_response(sum, status = 200)

app = web.Application()

app.router.add_post("/zbroj", handler_function)

web.run_app(app, port=8083)
