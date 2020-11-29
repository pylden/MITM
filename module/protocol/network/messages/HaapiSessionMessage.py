from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HaapiSessionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6833
        self.vars.append({"name": "key", "type": "String", "value": ""})
        self.vars.append({"name": "type", "type": "uint", "value": ""})
