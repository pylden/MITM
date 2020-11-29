from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeMoneyMovementInformationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1836
        self.vars.append({"name": "limit", "type": "Number", "value": ""})
