from module.protocol.network.messages.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage


class MapComplementaryInformationsAnomalyMessage(MapComplementaryInformationsDataMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        MapComplementaryInformationsDataMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6320
        self.vars.append({"name": "level", "type": "uint", "value": ""})
        self.vars.append({"name": "closingTime", "type": "Number", "value": ""})
