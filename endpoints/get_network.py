# encoding: utf-8

from server import cryptixd_client


async def get_network():
    """
    Get some global cryptix network information
    """
    resp = await cryptixd_client.request("getBlockDagInfoRequest")
    return resp["getBlockDagInfoResponse"]
