from module.protocol.network.messages.NetworkMessage import NetworkMessage


class EmoteListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7532
        self.emoteIds = {"type": "Vector.<uint>", "value": ""}
