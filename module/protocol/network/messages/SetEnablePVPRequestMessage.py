from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SetEnablePVPRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4606
        self.vars.append({"name": "enable", "type": "Boolean", "value": ""})
