from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismFightSwapRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5907
        self.vars.append({"name": "subAreaId", "type": "uint", "value": ""})
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
