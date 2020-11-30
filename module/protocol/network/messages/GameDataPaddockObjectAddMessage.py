from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameDataPaddockObjectAddMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7563
        self.paddockItemDescription = {"type": "PaddockItem", "value": ""}
