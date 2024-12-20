import asyncio
import aiohttp

async def operation(session, url, data):
    response = await session.post(url, json=data)
    response_data = await response.json()
    return response_data

async def main():
    async with aiohttp.ClientSession() as session:
        data = [1, 2, 3, 4, 5]
        task_1 = asyncio.create_task(operation(session, "http://localhost:8083/zbroj", data))
        task_2 = asyncio.create_task(operation(session, "http://localhost:8084/umnozak", data))

        rez = await asyncio.gather(task_1, task_2)
        print(rez[0], rez[1])

        rez_kol = await operation(session, "http://localhost:8085/kolicnik", rez)
        print(rez_kol)

asyncio.run(main())
