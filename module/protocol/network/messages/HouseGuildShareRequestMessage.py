from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HouseGuildShareRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 429
        self.houseId = {"type": "uint", "value": ""}
        self.instanceId = {"type": "uint", "value": ""}
        self.enable = {"type": "Boolean", "value": ""}
        self.rights = {"type": "uint", "value": ""}
