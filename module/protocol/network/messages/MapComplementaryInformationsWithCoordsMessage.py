from module.protocol.network.message import Message


class MapComplementaryInformationsWithCoordsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8121
        self.worldX = {"type": "int", "value": ""}
        self.worldY = {"type": "int", "value": ""}
