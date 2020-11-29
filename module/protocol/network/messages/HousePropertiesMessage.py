from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HousePropertiesMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5861
        self.vars.append({"name": "houseId", "type": "uint", "value": ""})
        self.vars.append({"name": "doorsOnMap", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "properties", "type": "HouseInstanceInformations", "value": ""})
