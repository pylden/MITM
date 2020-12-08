import asyncio


class Client(asyncio.Protocol):
    def __init__(self, server, protocol_processor_class, _distant_server_ip, _distant_server_port):
        asyncio.Protocol.__init__(self)
        self.protocol_processor = protocol_processor_class(self)
        self._server = server
        loop = asyncio.get_event_loop()
        client = loop.create_connection(lambda: self, _distant_server_ip, _distant_server_port)
        asyncio.ensure_future(client)

    def connection_made(self, transport):
        self.peername = transport.get_extra_info('peername')
        self.transport = transport
        print("Client connection_made: {}".format(self.peername))

    def data_received(self, data):  # Data received from distant server
        self.write_local(self.protocol_processor.from_server(data))  # From distant server server to local server to client

    def from_client(self, data):  # Data received from local server
        self.write_distant(self.protocol_processor.from_client(data))  # From client to local server to distant server

    def write_distant(self, buffer):
        if buffer:
            self.transport.write(buffer)

    def write_local(self, buffer):
        if buffer:
            self._server.transport.write(buffer)

    def connection_lost(self, exc):
        print("Client disconnected")

    def disconnect_from_distant(self):
        self.transport.close()

    def disconnect_from_local(self):
        self._server.transport.close()

    def disconnect_all(self):
        self.disconnect_from_distant()
        self.disconnect_from_local()
