from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChannelEnablingMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9158
        self.channel = {"type": "uint", "value": ""}
        self.enable = {"type": "Boolean", "value": ""}
