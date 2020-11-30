from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HavenBagFurnituresRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1534
        self.cellIds = {"type": "Vector.<uint>", "value": ""}
        self.funitureIds = {"type": "Vector.<int>", "value": ""}
        self.orientations = {"type": "Vector.<uint>", "value": ""}
