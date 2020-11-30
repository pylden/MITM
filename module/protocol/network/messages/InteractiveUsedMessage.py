from module.protocol.network.messages.NetworkMessage import NetworkMessage


class InteractiveUsedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9839
        self.entityId = {"type": "Number", "value": ""}
        self.elemId = {"type": "uint", "value": ""}
        self.skillId = {"type": "uint", "value": ""}
        self.duration = {"type": "uint", "value": ""}
        self.canMove = {"type": "Boolean", "value": ""}
