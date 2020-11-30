from module.protocol.network.messages.NetworkMessage import NetworkMessage


class InteractiveUseRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3724
        self.elemId = {"type": "uint", "value": ""}
        self.skillInstanceUid = {"type": "uint", "value": ""}
