class ProtocolProcessor:
    def __init__(self, client):
        self._server_buffer = self._client_buffer = bytes()
        self._client = client

    def from_client(self, data):
        pass

    def from_server(self, data):
        pass
