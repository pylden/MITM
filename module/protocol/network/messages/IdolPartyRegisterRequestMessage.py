from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IdolPartyRegisterRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5600
        self.register = {"type": "Boolean", "value": ""}
