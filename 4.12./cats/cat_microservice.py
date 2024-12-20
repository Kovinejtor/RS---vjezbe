from aiohttp import web 
import aiohttp
import asyncio

async def get_cat_fact(session):
    async with session.get("https://catfact.ninja/fact") as response:
        data = await response.json()
        return data.get("fact")

async def get_cat_facts(request):
    amount = int(request.match_info.get("amount"))
        
    async with aiohttp.ClientSession() as session:
        tasks = [get_cat_fact(session) for _ in range(amount)]
        facts = await asyncio.gather(*tasks)
        
        return web.json_response({"facts": facts}, status=200)

app = web.Application()

app.router.add_get("/cats/{amount}", get_cat_facts)

web.run_app(app, port=8086)
