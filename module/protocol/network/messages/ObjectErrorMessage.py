from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ObjectErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5736
        self.reason = {"type": "int", "value": ""}
