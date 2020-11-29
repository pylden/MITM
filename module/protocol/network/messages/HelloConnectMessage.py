from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HelloConnectMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2607
        self.vars.append({"name": "salt", "type": "String", "value": ""})
        self.vars.append({"name": "key", "type": "Vector.<int>", "value": ""})
