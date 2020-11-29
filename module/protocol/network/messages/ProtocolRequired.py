from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ProtocolRequired(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5481
        self.vars.append({"name": "version", "type": "String", "value": ""})
