from module.protocol.network.messages.NetworkMessage import NetworkMessage


class InteractiveUseEndedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 785
        self.elemId = {"type": "uint", "value": ""}
        self.skillId = {"type": "uint", "value": ""}
