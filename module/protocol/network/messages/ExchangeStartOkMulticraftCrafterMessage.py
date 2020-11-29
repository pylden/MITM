from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartOkMulticraftCrafterMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9643
        self.vars.append({"name": "skillId", "type": "uint", "value": ""})
