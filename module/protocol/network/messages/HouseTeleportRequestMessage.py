from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HouseTeleportRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6194
        self.vars.append({"name": "houseId", "type": "uint", "value": ""})
        self.vars.append({"name": "houseInstanceId", "type": "uint", "value": ""})
