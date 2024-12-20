import aiohttp
import asyncio

async def fetch_cat_facts(amount):
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:8086/cats/{amount}".format(amount=amount)) as response:
            data = await response.json()
            return data.get("facts", [])

async def filter_cat_facts(facts):
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8087/facts", json={"facts": facts}) as response:
            data = await response.json()
            return data.get("filtered_facts", [])

async def main():
    amount = 5

    facts = await fetch_cat_facts(amount)
    filtered_facts = await filter_cat_facts(facts)
    
    print(f"Filtered facts: {filtered_facts}")

asyncio.run(main())
