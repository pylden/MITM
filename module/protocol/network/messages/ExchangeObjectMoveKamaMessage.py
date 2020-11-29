from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeObjectMoveKamaMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4713
        self.vars.append({"name": "quantity", "type": "Number", "value": ""})
