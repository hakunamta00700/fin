import time
import os
import click

from .libs.tickers import save_tickers, load_tickers
from .crawl import main
import asyncio


@click.command()
@click.option('--filename', prompt="input filename to save result", help="get_result", required=True)
def get_tickerlist(filename):
    start_time = time.time()
    save_tickers(fn=filename)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"함수 실행 시간: {elapsed_time}초")


@click.command()
@click.option("--filename", prompt="filename which is saved tickers info", required=True)
@click.option("--output", prompt="input filename to save result", required=True)
def get_stockinfo_list(filename, output):
    if not os.path.exists(filename):
        raise FileNotFoundError(filename)
    stock_list = load_tickers(fn=filename)
    asyncio.run(main(stock_list, output))
