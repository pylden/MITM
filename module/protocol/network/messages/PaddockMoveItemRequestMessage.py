from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PaddockMoveItemRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 815
        self.oldCellId = {"type": "uint", "value": ""}
        self.newCellId = {"type": "uint", "value": ""}
