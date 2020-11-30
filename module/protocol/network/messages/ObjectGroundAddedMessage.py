from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ObjectGroundAddedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8648
        self.cellId = {"type": "uint", "value": ""}
        self.objectGID = {"type": "uint", "value": ""}
