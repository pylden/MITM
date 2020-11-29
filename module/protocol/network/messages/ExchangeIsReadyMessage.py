from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeIsReadyMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2446
        self.vars.append({"name": "id", "type": "Number", "value": ""})
        self.vars.append({"name": "ready", "type": "Boolean", "value": ""})
