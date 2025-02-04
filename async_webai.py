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


async def main(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        loop = asyncio.get_event_loop()
        links = await parse(html,loop)
        # Do something with the results
        print(links)


url = "https://www.fpds.gov/ezsearch/fpdsportal?q=SECURITIES+AND+EXCHANGE+COMMISSION&s=FPDS.GOV&templateName=1.5.3&indexName=awardfull&x=19&y=13"  # Replace with your target URL
asyncio.run(main(url))