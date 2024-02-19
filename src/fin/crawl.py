import codecs

import aiohttp
from bs4 import BeautifulSoup
from tqdm import tqdm


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_pbr_and_roe(session, stock_number, name):
    url = f"https://www.valueline.co.kr/finance/balancesheet/{stock_number}"
    html = await fetch(session, url)
    soup = BeautifulSoup(html, "html.parser")

    pbr_element = soup.select_one(".dtcon ul li:nth-of-type(4) dd")
    roe_element = soup.select_one(".dtcon ul li:nth-of-type(5) dd")

    pbr = pbr_element.text.replace("배", "") if pbr_element else "NOT_FOUND"
    roe = roe_element.text.replace("%", "") if roe_element else "NOT_FOUND"

    return {"stock_number": stock_number, "name": name, "PBR": pbr, "ROE": roe}


async def main(stock_numbers, save_fn):
    fp = codecs.open(save_fn, "w", "utf_8")
    async with aiohttp.ClientSession() as session:
        for code, name in tqdm(stock_numbers[:100]):
            result = await get_pbr_and_roe(session, code, name)
            fp.write(f"{code}\t{name}\t{result['PBR']}\t{result['ROE']}\n")
