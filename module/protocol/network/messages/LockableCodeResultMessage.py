from module.protocol.network.messages.NetworkMessage import NetworkMessage


class LockableCodeResultMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 302
        self.result = {"type": "uint", "value": ""}
