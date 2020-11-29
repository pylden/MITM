from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MountSetXpRatioRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4309
        self.vars.append({"name": "xpRatio", "type": "uint", "value": ""})
