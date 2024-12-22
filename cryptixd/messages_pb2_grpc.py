# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import messages_pb2 as messages__pb2


class P2PStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MessageStream = channel.stream_stream(
                '/protowire.P2P/MessageStream',
                request_serializer=messages__pb2.CryptixdMessage.SerializeToString,
                response_deserializer=messages__pb2.CryptixdMessage.FromString,
                )


class P2PServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MessageStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_P2PServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MessageStream': grpc.stream_stream_rpc_method_handler(
                    servicer.MessageStream,
                    request_deserializer=messages__pb2.CryptixdMessage.FromString,
                    response_serializer=messages__pb2.CryptixdMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protowire.P2P', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class P2P(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MessageStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/protowire.P2P/MessageStream',
            messages__pb2.CryptixdMessage.SerializeToString,
            messages__pb2.CryptixdMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class RPCStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MessageStream = channel.stream_stream(
                '/protowire.RPC/MessageStream',
                request_serializer=messages__pb2.CryptixdMessage.SerializeToString,
                response_deserializer=messages__pb2.CryptixdMessage.FromString,
                )


class RPCServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MessageStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MessageStream': grpc.stream_stream_rpc_method_handler(
                    servicer.MessageStream,
                    request_deserializer=messages__pb2.CryptixdMessage.FromString,
                    response_serializer=messages__pb2.CryptixdMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protowire.RPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RPC(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MessageStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/protowire.RPC/MessageStream',
            messages__pb2.CryptixdMessage.SerializeToString,
            messages__pb2.CryptixdMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
