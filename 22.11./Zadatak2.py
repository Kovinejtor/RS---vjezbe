# 2. Definirajte dvije korutine, od kojih će jedna služiti za dohvaćanje činjenica o mačkama koristeći
# get_cat_fact korutinu koja šalje GET zahtjev na URL: https://catfact.ninja/fact . Izradite 20
# Task objekata za dohvaćanje činjenica o mačkama te ih pozovite unutar main korutine i rezultate
# pohranite odjednom koristeći asyncio.gather funkciju. Druga korutina filter_cat_facts ne šalje
# HTTP zahtjeve, već mora primiti gotovu listu činjenica o mačkama i vratiti novu listu koja sadrži samo
# one činjenice koje sadrže riječ "cat" ili "cats" (neovisno o velikim/malim slovima).

import asyncio
import aiohttp

async def get_cat_fact(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return data["fact"]

async def filtered_cat_facts(facts):
    filtered_facts = [fact for fact in facts if "cat" in fact.lower() or "cats" in fact.lower()]
    return filtered_facts

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [get_cat_fact(session, "https://catfact.ninja/fact") for i in range(20)]
        facts = await asyncio.gather(*tasks)

    print(f"All cat facts: {facts}")
    print("\n")

    filtered_facts = await filtered_cat_facts(facts)
    print(f"Filtered cat facts: {filtered_facts}")

asyncio.run(main())
