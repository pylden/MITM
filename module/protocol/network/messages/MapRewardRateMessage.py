from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MapRewardRateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9715
        self.vars.append({"name": "mapRate", "type": "int", "value": ""})
        self.vars.append({"name": "subAreaRate", "type": "int", "value": ""})
        self.vars.append({"name": "totalRate", "type": "int", "value": ""})
