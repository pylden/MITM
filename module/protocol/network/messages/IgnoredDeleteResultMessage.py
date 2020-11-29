from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IgnoredDeleteResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5614
        self.vars.append({"name": "success", "type": "Boolean", "value": ""})
        self.vars.append({"name": "name", "type": "String", "value": ""})
        self.vars.append({"name": "session", "type": "Boolean", "value": ""})
