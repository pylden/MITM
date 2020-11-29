from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MountDataMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8157
        self.vars.append({"name": "mountData", "type": "MountClientData", "value": ""})
