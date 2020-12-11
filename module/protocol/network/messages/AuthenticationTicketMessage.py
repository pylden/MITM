from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AuthenticationTicketMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8374
        self.lang = {"type": "String", "value": ""}
        self.ticket = {"type": "String", "value": ""}

    def deserialize(self):
        self.lang = self.buffer_reader.read_utf()
        self.ticket = self.buffer_reader.read_utf()
