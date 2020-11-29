from module.protocol.network.messages.NetworkMessage import NetworkMessage


class LockableUseCodeMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 632
        self.vars.append({"name": "code", "type": "String", "value": ""})
