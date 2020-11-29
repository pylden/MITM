from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3594
        self.vars.append({"name": "errorType", "type": "int", "value": ""})
