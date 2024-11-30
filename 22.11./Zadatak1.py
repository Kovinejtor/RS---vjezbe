# 1. Definirajte korutinu fetch_users koja će slati GET zahtjev na JSONPlaceholder API na URL-u:
# https://jsonplaceholder.typicode.com/users . Morate simulirate slanje 5 zahtjeva konkurentno
# unutar main korutine. Unutar main korutine izmjerite vrijeme izvođenja programa, a rezultate
# pohranite u listu odjedanput koristeći asyncio.gather funkciju. Nakon toga koristeći map funkcije ili
# list comprehension izdvojite u zasebne 3 liste: samo imena korisnika, samo email adrese korisnika i
# samo username korisnika. Na kraju main korutine ispišite sve 3 liste i vrijeme izvođenja programa.

import asyncio
import aiohttp
import time

async def fetch_users(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_users(session, "https://jsonplaceholder.typicode.com/users") for i in range(5)]
        results = await asyncio.gather(*tasks)

    users = results[0]
    
    names = [user["name"] for user in users]
    emails = [user["email"] for user in users]
    usernames = [user["username"] for user in users]
    end = time.time()
    
    print("Names:", names)
    print("Emails:", emails)
    print("Usernames:", usernames)
    print(f"Time: {end - start} seconds")

asyncio.run(main())
