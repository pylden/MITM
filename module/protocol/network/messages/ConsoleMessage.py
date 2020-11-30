from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ConsoleMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3514
        self.type = {"type": "uint", "value": ""}
        self.content = {"type": "String", "value": ""}
