from module.protocol.network.messages.NetworkMessage import NetworkMessage


class WarnOnPermaDeathStateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2119
        self.enable = {"type": "Boolean", "value": ""}
