from module.protocol.network.message import Message


class MapComplementaryInformationsWithCoordsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8121
        self.worldX = {"type": "int", "value": ""}
        self.worldY = {"type": "int", "value": ""}
