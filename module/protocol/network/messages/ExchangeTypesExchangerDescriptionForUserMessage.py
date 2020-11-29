from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeTypesExchangerDescriptionForUserMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9562
        self.vars.append({"name": "objectType", "type": "uint", "value": ""})
        self.vars.append({"name": "typeDescription", "type": "Vector.<uint>", "value": ""})
