from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MimicryObjectPreviewMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1082
        self.result = {"type": "ObjectItem", "value": ""}
