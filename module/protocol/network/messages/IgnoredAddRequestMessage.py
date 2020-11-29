from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IgnoredAddRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9784
        self.vars.append({"name": "name", "type": "String", "value": ""})
        self.vars.append({"name": "session", "type": "Boolean", "value": ""})
