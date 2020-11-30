from module.protocol.network.messages.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage


class MapComplementaryInformationsBreachMessage(MapComplementaryInformationsDataMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        MapComplementaryInformationsDataMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5079
        self.floor = {"type": "uint", "value": ""}
        self.room = {"type": "uint", "value": ""}
        self.infinityMode = {"type": "uint", "value": ""}
        self.branches = {"type": "Vector.<BreachBranch>", "value": ""}
