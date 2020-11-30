from module.protocol.network.messages.NetworkMessage import NetworkMessage


class StatedElementUpdatedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4169
        self.statedElement = {"type": "StatedElement", "value": ""}
