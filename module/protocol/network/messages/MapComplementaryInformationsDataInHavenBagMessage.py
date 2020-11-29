from module.protocol.network.messages.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage


class MapComplementaryInformationsDataInHavenBagMessage(MapComplementaryInformationsDataMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        MapComplementaryInformationsDataMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3465
        self.vars.append({"name": "ownerInformations", "type": "CharacterMinimalInformations", "value": ""})
        self.vars.append({"name": "theme", "type": "int", "value": ""})
        self.vars.append({"name": "roomId", "type": "uint", "value": ""})
        self.vars.append({"name": "maxRoomId", "type": "uint", "value": ""})
