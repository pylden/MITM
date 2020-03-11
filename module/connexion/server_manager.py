from module.connexion.server import Server
import asyncio
from threading import Thread


class ServerManager:
    def __init__(self, server_host, server_port, client_host, client_port, protocol_processor):
        self._s_host = server_host
        self._s_port = server_port
        self._c_host = client_host
        self._c_port = client_port
        self._protocol_processor = protocol_processor
        self._server = None
        self._loop = asyncio.get_event_loop()
        self._thread = Thread(target=self.start_server)

    def start_server(self):
        coro = self._loop.create_server(lambda: Server(self._protocol_processor, self._c_host, self._c_port),
                                        self._s_host, self._s_port)
        self._server = self._loop.run_until_complete(coro)
        for socket in self._server.sockets:
            print("serving on {0}".format(socket.getsockname()))
        self._loop.run_forever()

    def start_server_in_thread(self):
        self._thread.start()
