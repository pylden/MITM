from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CompassResetMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2894
        self.type = {"type": "uint", "value": ""}
