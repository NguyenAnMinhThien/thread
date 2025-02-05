import time

import aiohttp
import asyncio

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()
                print(f"URL: {url}, Data: {data[:50]}...")  # Truncate for brevity
            else:
                print(f"Error fetching {url}: {response.status}")

async def main(urls):
    tasks = [asyncio.create_task(fetch_url(url)) for url in urls]
    await asyncio.gather(*tasks)


mylist = list()
for i in range(0,1000):
    mylist.append(i*30)

urls = [
    f"https://www.fpds.gov/ezsearch/fpdsportal?q=SECURITIES+AND+EXCHANGE+COMMISSION&s=FPDS.GOV&templateName=1.5.3&indexName=awardfull&x=19&y=13&start={number}"
    for number in mylist]
start = time.time()
asyncio.run(main(urls))
end = time.time()
print(f"Total time: {end - start}")
