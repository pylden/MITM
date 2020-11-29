from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeHandleMountsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3008
        self.vars.append({"name": "actionType", "type": "int", "value": ""})
        self.vars.append({"name": "ridesId", "type": "Vector.<uint>", "value": ""})
