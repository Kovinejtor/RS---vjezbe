from aiohttp import web 

async def handler_function(request):
    request_data = await request.json()
    if request_data[1] == 0:
        return web.json_response({"error": "division with 0 is not allowed"}, status = 400)

    kolicnik = request_data[1] / request_data[0]
    return web.json_response(kolicnik, status = 200)

app = web.Application()

app.router.add_post("/kolicnik", handler_function)

web.run_app(app, port=8085)
