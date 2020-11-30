from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChatAbstractClientMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8438
        self.content = {"type": "String", "value": ""}
