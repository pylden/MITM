class Bot:
    def __init__(self, client):
        self._client_counting = 0
        self._connected = False
        self._authenticated = False
        self._data_character = {}
        self._client = client

    def read_messages(self, messages):
        data = ''
        for message in messages:
            if message.id == 6182:
                self.read_SelectedServerDataMessage(message)
                return None
            if 'read_%s' % type(message).__name__ in dir(self):
                data += getattr(self, 'read_%s' % type(message).__name__)(message)
            else:
                data += message.get_data().hex()
        return bytes.fromhex(data)

    def read_SelectedServerDataMessage(self, message):
        message.address["value"] = "127.0.0.1"
        message.serialize()
        self._client.write_local(bytes.fromhex(message.get_data().hex()))
        self._client.disconnect_all()
