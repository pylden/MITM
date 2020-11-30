from module.protocol.network.messages.NetworkMessage import NetworkMessage


class EmotePlayAbstractMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7499
        self.emoteId = {"type": "uint", "value": ""}
        self.emoteStartTime = {"type": "Number", "value": ""}
