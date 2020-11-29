from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HavenBagFurnituresRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1534
        self.vars.append({"name": "cellIds", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "funitureIds", "type": "Vector.<int>", "value": ""})
        self.vars.append({"name": "orientations", "type": "Vector.<uint>", "value": ""})
