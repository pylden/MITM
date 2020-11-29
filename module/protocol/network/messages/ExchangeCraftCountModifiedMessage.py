from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeCraftCountModifiedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3547
        self.vars.append({"name": "count", "type": "int", "value": ""})
