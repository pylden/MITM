from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MapInformationsRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2540
        self.vars.append({"name": "mapId", "type": "Number", "value": ""})
