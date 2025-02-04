import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Perform your scraping tasks here
    # For example, to find all 'a' tags:
    links = soup.find_all('a')
    # Do something with the links
    return links

async def main(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        links = await parse(html)
        # Do something with the results
        print(links)

url = "https://www.fpds.gov/ezsearch/fpdsportal?q=SECURITIES+AND+EXCHANGE+COMMISSION&s=FPDS.GOV&templateName=1.5.3&indexName=awardfull&x=19&y=13"  # Replace with your target URL
asyncio.run(main(url))