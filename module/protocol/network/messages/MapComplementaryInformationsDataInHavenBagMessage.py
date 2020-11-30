from module.protocol.network.messages.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage


class MapComplementaryInformationsDataInHavenBagMessage(MapComplementaryInformationsDataMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        MapComplementaryInformationsDataMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3465
        self.ownerInformations = {"type": "CharacterMinimalInformations", "value": ""}
        self.theme = {"type": "int", "value": ""}
        self.roomId = {"type": "uint", "value": ""}
        self.maxRoomId = {"type": "uint", "value": ""}
