from module.protocol.network.messages.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage


class MapComplementaryInformationsWithCoordsMessage(MapComplementaryInformationsDataMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        MapComplementaryInformationsDataMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8121
        self.worldX = {"type": "int", "value": ""}
        self.worldY = {"type": "int", "value": ""}
