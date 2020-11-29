from module.protocol.network.messages.NetworkMessage import NetworkMessage


class LockableChangeCodeMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7253
        self.vars.append({"name": "code", "type": "String", "value": ""})
