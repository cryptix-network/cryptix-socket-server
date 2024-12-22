# encoding: utf-8
import requests
from cachetools.func import ttl_cache


@ttl_cache(ttl=60)
def get_cytx_price():
    resp = requests.get("https://api.coingecko.com/api/v3/simple/price",
                        params={"ids": "cryptix",
                                "vs_currencies": "usd"})
    if resp.status_code == 200:
        return resp.json()["cryptix"]["usd"]

@ttl_cache(ttl=60)
def get_cytx_market_data():
    resp = requests.get("https://api.coingecko.com/api/v3/coins/cryptix")
    if resp.status_code == 200:
        return resp.json()["market_data"]