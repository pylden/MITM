from module.protocol.network.messages.NetworkMessage import NetworkMessage


class LivingObjectMessageMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9436
        self.msgId = {"type": "uint", "value": ""}
        self.timeStamp = {"type": "uint", "value": ""}
        self.owner = {"type": "String", "value": ""}
        self.objectGenericId = {"type": "uint", "value": ""}
