import asyncio


class Client(asyncio.Protocol):
    def __init__(self, server, protocol_processor_class):
        asyncio.Protocol.__init__(self)
        self.protocol_processor = protocol_processor_class(self)
        self._server = server

    def connection_made(self, transport):
        self.peername = transport.get_extra_info('peername')
        self.transport = transport
        print("Client connection_made: {}".format(self.peername))

    def data_received(self, data):  # Data received from distant server
        self.protocol_processor.from_server(data)
        self._server.transport.write(data)  # From distant server server to local server

    def from_client(self, data):  # Data received from local server
        self.protocol_processor.from_client(data)
        self.write(data)  # From local server to distant server

    def write(self, buffer):
        self.transport.write(buffer)

    def connection_lost(self, exc):
        print("Client disconnected")
