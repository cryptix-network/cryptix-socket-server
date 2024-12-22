# encoding: utf-8

from server import cryptixd_client


async def get_coinsupply():
    """
    Get $CYTX coin supply information
    """
    resp = await cryptixd_client.request("getCoinSupplyRequest")
    return {
        "circulatingSupply": resp["getCoinSupplyResponse"]["circulatingSompi"],
        "totalSupply": resp["getCoinSupplyResponse"]["circulatingSompi"],
        "maxSupply": resp["getCoinSupplyResponse"]["maxSompi"]
    }


async def get_circulating_coins(in_billion: bool = False):
    """
    Get circulating amount of $CYTX token as numerical value
    """
    resp = await cryptixd_client.request("getCoinSupplyRequest")
    coins = str(float(resp["getCoinSupplyResponse"]["circulatingSompi"]) / 100000000)
    if in_billion:
        return str(round(float(coins) / 1000000000, 2))
    else:
        return coins


async def get_circulating_coins():
    """
    Get total amount of $CYTX token as numerical value
    """
    resp = await cryptixd_client.request("getCoinSupplyRequest")
    return str(float(resp["getCoinSupplyResponse"]["circulatingSompi"]) / 100000000)
