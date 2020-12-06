class Bot:
    def __init__(self):
        self._client_counting = 0
        self._connected = False
        self._authenticated = False
        self._data_character = {}

    def read_server_messages(self, messages):
        pass

    def read_client_messages(self, messages):
        pass
