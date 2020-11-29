from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ConsoleMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3514
        self.vars.append({"name": "type", "type": "uint", "value": ""})
        self.vars.append({"name": "content", "type": "String", "value": ""})
