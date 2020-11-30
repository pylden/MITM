from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HousePropertiesMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5861
        self.houseId = {"type": "uint", "value": ""}
        self.doorsOnMap = {"type": "Vector.<uint>", "value": ""}
        self.properties = {"type": "HouseInstanceInformations", "value": ""}
