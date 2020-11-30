from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ShowCellMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7767
        self.sourceId = {"type": "Number", "value": ""}
        self.cellId = {"type": "uint", "value": ""}
