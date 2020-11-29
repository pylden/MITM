from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismFightRemovedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6587
        self.vars.append({"name": "subAreaId", "type": "uint", "value": ""})
