from module.connexion.client import Client
import asyncio


class Server(asyncio.Protocol):  # MITM Server
    clients = []

    def __init__(self, protocol_processor_class, distant_server_ip, distant_server_port):
        asyncio.Protocol.__init__(self)
        self._client = None
        self._protocol_processor_class = protocol_processor_class
        self._distant_server_ip = distant_server_ip
        self._distant_server_port = distant_server_port

    def connection_made(self, transport):
        self.transport = transport
        self.peername = transport.get_extra_info("peername")
        self._client = Client(self, self._protocol_processor_class)
        self.__class__.clients.append({'id': None, 'instance': self._client})

        loop = asyncio.get_event_loop()
        client = loop.create_connection(lambda: self._client, self._distant_server_ip, self._distant_server_port)
        print("Server connection_made: {}".format(self.peername))
        asyncio.ensure_future(client)

    def data_received(self, data):  # Data received from client
        self._client.from_client(data)

    def connection_lost(self, exc):
        print("Connection lost")
        self._client.transport.close()
