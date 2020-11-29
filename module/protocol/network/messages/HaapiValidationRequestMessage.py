from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HaapiValidationRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9199
        self.vars.append({"name": "transaction", "type": "String", "value": ""})
