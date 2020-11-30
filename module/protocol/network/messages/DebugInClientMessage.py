from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DebugInClientMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1327
        self.level = {"type": "uint", "value": ""}
        self.message = {"type": "String", "value": ""}
