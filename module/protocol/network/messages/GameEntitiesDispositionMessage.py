from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameEntitiesDispositionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1072
        self.dispositions = {"type": "Vector.<IdentifiedEntityDispositionInformations>", "value": ""}
