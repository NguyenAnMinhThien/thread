import asyncio
import multiprocessing
import os
import psutil
import threading
import time
from bs4 import BeautifulSoup
import pandas
import os
import requests
session = requests.Session()
async def load_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'}
    try:
        async with session.get(url=url, headers=headers) as r:
            if await r.status_code == 200:
                return await r
    except Exception as e:
        print("Something wrong.", e)


# this function include the tasks require more time
async def extract_page(url):
    print(f"Is scraping data at Lawyer profile : {url}")
    r = await load_page(url)
    soup = BeautifulSoup(r.content, features="html.parser")
    tables = soup.find_all(class_="resultbox1")
    print(tables[0])


async def print_info(value):
    await extract_page("https://www.fpds.gov/ezsearch/fpdsportal?q=SECURITIES+AND+EXCHANGE+COMMISSION&s=FPDS.GOV&templateName=1.5.3&indexName=awardfull&x=19&y=13")
    print(
        f"THREAD: {threading.get_ident()}",
        f"PROCESS: {os.getpid()}",
        f"VALUE: {value}",
    )

async def await_async_logic(values):
    await asyncio.gather(
        *(
            print_info(value)
            for value in values
        )
    )

def run_async_logic(values):
    asyncio.run(await_async_logic(values))

def multiprocessing_executor():
    start = time.time()
    with multiprocessing.Pool() as multiprocessing_pool:
        # map with each value of generator object to a normal function - inside this function, it include
        multiprocessing_pool.map(
            run_async_logic,
            (range(10 * x, 10 * (x + 1)) for x in range(os.cpu_count())),
        )
    end = time.time()
    print(end - start)
if __name__ == '__main__':
    multiprocessing_executor()
