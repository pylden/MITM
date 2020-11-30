from module.protocol.network.messages.NetworkMessage import NetworkMessage


class DebugHighlightCellsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1636
        self.color = {"type": "Number", "value": ""}
        self.cells = {"type": "Vector.<uint>", "value": ""}
