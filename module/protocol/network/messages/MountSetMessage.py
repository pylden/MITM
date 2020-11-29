from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MountSetMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8199
        self.vars.append({"name": "mountData", "type": "MountClientData", "value": ""})
