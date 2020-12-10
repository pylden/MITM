class ProtocolProcessor:
    def __init__(self, client):
        self._server_buffer = self._client_buffer = bytes()
        self._client = client
        self.view = None

    def from_client(self, data):
        """Action when client send data"""
        pass

    def from_server(self, data):
        """Action when server send data"""
        pass
