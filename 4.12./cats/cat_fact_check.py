from aiohttp import web

async def filtering_cat_facts(request):
    request_data = await request.json()
    facts = request_data.get("facts", [])
    
    filtered_facts = [fact for fact in facts if "cat" in fact.lower()]
    
    return web.json_response({"filtered_facts": filtered_facts}, status=200)

app = web.Application()

app.router.add_post("/facts", filtering_cat_facts)

web.run_app(app, port=8087)
