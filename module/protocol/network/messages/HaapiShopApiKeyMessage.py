from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HaapiShopApiKeyMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6552
        self.vars.append({"name": "token", "type": "String", "value": ""})
