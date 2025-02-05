import asyncio
import time
from aiohttp import ClientSession, ClientResponseError


async def fetch_url_data(session, url):
  try:
    async with session.get(url, timeout=60) as response:
      resp = await response.text()
      print(resp[:50])
  except Exception as e:
    print(e)
  else:
    return resp
  return


async def fetch_async(loop):

  mylist = list()
  for i in range(0,1000):
    mylist.append(i*30)
  urls = [
  f"https://www.fpds.gov/ezsearch/fpdsportal?q=SECURITIES+AND+EXCHANGE+COMMISSION&s=FPDS.GOV&templateName=1.5.3&indexName=awardfull&x=19&y=13&start={number}"
  for number in mylist]
  tasks = []
  async with ClientSession() as session:
    for url in urls:
      task = asyncio.ensure_future(fetch_url_data(session, url))
      tasks.append(task)
    responses = await asyncio.gather(*tasks)
  return responses


if __name__ == '__main__':
  # for ntimes in [1, 10, 50, 100, 500]:
    start_time = time.time()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(fetch_async(loop))
    loop.run_until_complete(future) #will run until it finish or get any error
    responses = future.result()
    print(f'Fetch total urls and process takes {time.time() - start_time} seconds')
