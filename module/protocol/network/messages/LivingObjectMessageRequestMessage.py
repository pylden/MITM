from module.protocol.network.messages.NetworkMessage import NetworkMessage


class LivingObjectMessageRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4103
        self.msgId = {"type": "uint", "value": ""}
        self.parameters = {"type": "Vector.<String>", "value": ""}
        self.livingObject = {"type": "uint", "value": ""}
