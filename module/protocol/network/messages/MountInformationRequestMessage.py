from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MountInformationRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5729
        self.id = {"type": "Number", "value": ""}
        self.time = {"type": "Number", "value": ""}
