from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HaapiCancelBidRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9408
        self.vars.append({"name": "id", "type": "Number", "value": ""})
        self.vars.append({"name": "type", "type": "uint", "value": ""})
