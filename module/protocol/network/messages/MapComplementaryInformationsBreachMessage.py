from module.protocol.network.messages.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage


class MapComplementaryInformationsBreachMessage(MapComplementaryInformationsDataMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        MapComplementaryInformationsDataMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5079
        self.vars.append({"name": "floor", "type": "uint", "value": ""})
        self.vars.append({"name": "room", "type": "uint", "value": ""})
        self.vars.append({"name": "infinityMode", "type": "uint", "value": ""})
        self.vars.append({"name": "branches", "type": "Vector.<BreachBranch>", "value": ""})
