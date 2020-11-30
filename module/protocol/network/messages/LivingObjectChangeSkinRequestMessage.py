from module.protocol.network.messages.NetworkMessage import NetworkMessage


class LivingObjectChangeSkinRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1423
        self.livingUID = {"type": "uint", "value": ""}
        self.livingPosition = {"type": "uint", "value": ""}
        self.skinId = {"type": "uint", "value": ""}
