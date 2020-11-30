from module.protocol.network.messages.NetworkMessage import NetworkMessage


class MountEquipedErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6900
        self.errorType = {"type": "uint", "value": ""}
