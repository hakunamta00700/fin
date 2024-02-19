import codecs
import datetime as dt

from pykrx import stock


def save_tickers(fn=None):
    """
    pykrx를 이용하여 종목번호, 종목명 리스트를 파일로 저장한다.
    """
    if fn:
        fp = codecs.open(fn, "w", "utf_8")
    today = dt.date.today().strftime("%Y%m%d")
    for ticker in stock.get_market_ticker_list(today, market="ALL"):
        name = stock.get_market_ticker_name(ticker)
        if fn:
            fp.write(f"{ticker}\t{name}\n")


def load_tickers(fn=None):
    """
    번호, 종목명 ....

    이런 형태의 리스트로 넘긴다.
    """
    output = []
    if fn:
        with codecs.open(fn, "r", "utf_8") as fp:
            for line in fp.readlines():
                _list = line.strip().split("\t")
                code = _list[0]
                name = _list[1]
                print(code, name)
                output.append([code, name])
        return output
