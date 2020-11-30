from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameDataPaddockObjectListAddMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3488
        self.paddockItemDescription = {"type": "Vector.<PaddockItem>", "value": ""}
