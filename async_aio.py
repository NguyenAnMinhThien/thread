import multiprocessing
import asyncio
import os
import psutil
import aiohttp
import threading
import time
from bs4 import BeautifulSoup
import pandas
import os
import requests

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

def parse(html):
    soup = BeautifulSoup(html,'html.parser')
    tables = soup.find_all(class_="resultbox1")
    return tables[0].text

async def fetch_and_parse(session, url):
    html = await fetch(session, url)
    paras = parse(html)
    return paras

async def scrape_urls(session,urls):
    await asyncio.gather(
        *(
            fetch_and_parse(session,url) for url in urls
        )
    )

mylist = list()
for i in range(0,2):
    mylist.append(i*30)

session = requests.Session()
urls = [
    f"https://www.fpds.gov/ezsearch/fpdsportal?q=SECURITIES+AND+EXCHANGE+COMMISSION&s=FPDS.GOV&templateName=1.5.3&indexName=awardfull&x=19&y=13&start={number}"
    for number in mylist]
asyncio.run(scrape_urls(urls))