# encoding: utf-8

from server import cryptixd_client


async def get_blockdag():
    """
    Get some global Cryptix BlockDAG information
    """
    resp = await cryptixd_client.request("getBlockDagInfoRequest")
    return resp["getBlockDagInfoResponse"]
