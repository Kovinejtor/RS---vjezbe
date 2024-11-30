# 3. Definirajte korutinu get_dog_fact koja dohvaća činjenice o psima sa DOG API.
# Korutina get_dog_fact neka dohvaća činjenicu o psima na URL-u: https://dogapi.dog/api/v2/facts .
# Nakon toga, definirajte korutinu get_cat_fact koja dohvaća činjenicu o mačkama slanjem zahtjeva na
# URL: https://catfact.ninja/fact .
# Istovremeno pohranite rezultate izvršavanja ovih Taskova koristeći asyncio.gather(*dog_facts_tasks,
# *cat_facts_tasks) funkciju u listu dog_cat_facts , a zatim ih koristeći list slicing odvojite u dvije liste
# obzirom da znate da je prvih 5 činjenica o psima, a drugih 5 o mačkama.
# Na kraju, definirajte i treću korutinu mix_facts koja prima liste dog_facts i cat_facts i vraća novu
# listu koja za vrijednost indeksa i sadrži činjenicu o psima ako je duljina činjenice o psima veća od duljine
# činjenice o mačkama na istom indeksu, inače vraća činjenicu o mački. Na kraju ispišite rezultate filtriranog
# niza činjenica. Liste možete paralelno iterirati koristeći zip funkciju, npr. for dog_fact, cat_fact in
# zip(dog_facts, cat_facts) .
# Primjer konačnog ispisa:
# Mixane činjenice o psima i mačkama:
# If they have ample water, cats can tolerate temperatures up to 133 °F.
# Dogs with little human contact in the first three months typically don’t make good pets.
# The most popular dog breed in Canada, U.S., and Great Britain is the Labrador retriever.
# An estimated 1,000,000 dogs in the U.S. have been named as the primary beneficiaries in
# their owner’s will.
# When a cats rubs up against you, the cat is marking you with it's scent claiming
# ownership.

import asyncio
import aiohttp

async def get_dog_fact(session, url="https://dogapi.dog/api/v2/facts"):
    async with session.get(url) as response:
        data = await response.json()
        return data["data"][0]["attributes"]["body"]

async def get_cat_fact(session, url="https://catfact.ninja/fact"):
    async with session.get(url) as response:
        data = await response.json()
        return data["fact"]

async def mix_facts(dog_facts, cat_facts):
    mixed_facts = [dog_fact if len(dog_fact) > len(cat_fact) else cat_fact for dog_fact, cat_fact in zip(dog_facts, cat_facts)]
    return mixed_facts

async def main():
    async with aiohttp.ClientSession() as session:
        dog_facts_tasks = [get_dog_fact(session) for i in range(5)]
        cat_facts_tasks = [get_cat_fact(session) for i in range(5)]

        dog_cat_facts = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)

    dog_facts = dog_cat_facts[:5]
    cat_facts = dog_cat_facts[5:]

    print("Dog Facts:", dog_facts)
    print("\n")
    print("Cat Facts:", cat_facts)
    print("\n")

    mixed_facts = await mix_facts(dog_facts, cat_facts)

    print("Facts about dogs and cats:")
    for fact in mixed_facts:
        print(fact)

asyncio.run(main())
