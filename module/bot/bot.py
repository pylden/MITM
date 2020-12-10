from module.connexion.server import Server


class Bot:
    def __init__(self, client):
        self.is_connected = False
        self.is_authenticated = False
        self.is_receiving_raw_data = False

        self._client_counting = 0
        self._data_character = {}
        self._client = client

        self.messages = []
        self.server = None
        self.port = None

    def is_reconnecting(self):
        return self.is_authenticated and not self.is_connected

    def reconnect_client(self, client):
        self._client = client

    def read_messages(self, messages):
        data = ''
        for message in messages:
            print(message.get_name())
            self.messages.append(message)
            if 'read_%s' % message.get_name() in dir(self):
                data += getattr(self, 'read_%s' % message.get_name())(message)
            else:
                data += message.get_data().hex()
            if message == "SelectedServerDataMessage":
                return None
        return bytes.fromhex(data)

    def read_SelectedServerDataMessage(self, message):
        self.server = message.address["value"]
        self.port = message.ports["value"][0]
        message.address["value"] = "127.0.0.1"
        message.serialize()
        self._client.write_local(bytes.fromhex(message.get_data().hex()))
        self.is_authenticated = True
        self._client.disconnect_all()
        self._client.reconnecting = True
        return ''

    def read_HelloGameMessage(self, message):
        self.is_connected = True
        return message.get_data().hex()

    def read_AuthenticationTicketMessage(self, message):
        print("ATM")
        self.is_receiving_raw_data = True
        return message.get_data().hex()
