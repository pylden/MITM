from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MountRenamedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7458
        self.mountId = {"type": "int", "value": ""}
        self.name = {"type": "String", "value": ""}
