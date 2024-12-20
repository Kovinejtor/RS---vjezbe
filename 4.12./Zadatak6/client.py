import asyncio
import aiohttp

async def cour(session, url, port):
    response = await session.get(url)
    response_data = await response.json()
    return response_data

async def main():
    async with aiohttp.ClientSession() as session:
       task_1 = asyncio.create_task(cour(session,"http://localhost:8081/pozdrav", 8081)) 
       task_2 = asyncio.create_task(cour(session,"http://localhost:8082/pozdrav", 8082)) 

       rez_1, rez_2 = await asyncio.gather(task_1, task_2)
       print("Prvi: ", rez_1)
       print("Drugi: ", rez_2)

    async with aiohttp.ClientSession() as session: 
        rez_1 = await cour(session,"http://localhost:8081/pozdrav", 8081)
        rez_2 = await cour(session,"http://localhost:8082/pozdrav", 8082)

        print("Prvi sekvencijalno: ", rez_1)
        print("Drugi sekvencijalno: ", rez_2)

asyncio.run(main())
