from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeReadyMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4086
        self.vars.append({"name": "ready", "type": "Boolean", "value": ""})
        self.vars.append({"name": "step", "type": "uint", "value": ""})
