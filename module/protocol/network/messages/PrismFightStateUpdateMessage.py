from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PrismFightStateUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1999
        self.vars.append({"name": "state", "type": "uint", "value": ""})
