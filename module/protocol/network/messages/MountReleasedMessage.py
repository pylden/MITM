from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MountReleasedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3002
        self.mountId = {"type": "int", "value": ""}
