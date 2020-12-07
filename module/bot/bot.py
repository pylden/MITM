class Bot:
    def __init__(self):
        self._client_counting = 0
        self._connected = False
        self._authenticated = False
        self._data_character = {}

    def read_messages(self, messages):
        data = ''
        for message in messages:
            if 'read_%s' % type(message).__name__ in dir(self):
                data += getattr(self, 'read_%s' % type(message).__name__)(message)
            else:
                data += message.get_original_data().hex()
        return bytes.fromhex(data)

    def read_SelectedServerDataMessage(self, message):
        message.address = "127.0.0.1"
        message.ports = [5555]
        return message.serialize()
