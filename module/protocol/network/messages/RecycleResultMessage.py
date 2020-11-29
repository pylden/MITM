from module.protocol.network.messages.NetworkMessage import NetworkMessage


class RecycleResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3014
        self.vars.append({"name": "nuggetsForPrism", "type": "uint", "value": ""})
        self.vars.append({"name": "nuggetsForPlayer", "type": "uint", "value": ""})
