import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

import concurrent.futures

async def parse(html,loop):
    # Use default executor (ThreadPoolExecutor) to run synchronous code
    soup = await loop.run_in_executor(None, BeautifulSoup, html, 'html.parser')
    links = soup.find_all('a')
    return links

async def fetch_and_parse(session, url):
    html = await fetch(session, url)
    loop = asyncio.get_event_loop()
    links = await parse(html, loop)
    # Do something with the results
    print(links)


async def main(urls):
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *(
                fetch_and_parse(session, url) for url in urls
            )
        )


mylist = list()
for i in range(0,20):
    mylist.append(i*30)

urls = [
    f"https://www.fpds.gov/ezsearch/fpdsportal?q=SECURITIES+AND+EXCHANGE+COMMISSION&s=FPDS.GOV&templateName=1.5.3&indexName=awardfull&x=19&y=13&start={number}"
    for number in mylist]

asyncio.run(main(urls))