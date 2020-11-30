from module.protocol.network.messages.NetworkMessage import NetworkMessage


class EnabledChannelsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2771
        self.channels = {"type": "Vector.<uint>", "value": ""}
        self.disallowed = {"type": "Vector.<uint>", "value": ""}
