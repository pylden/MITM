from module.protocol.network.messages.NetworkMessage import NetworkMessage


class CinematicMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4277
        self.cinematicId = {"type": "uint", "value": ""}
