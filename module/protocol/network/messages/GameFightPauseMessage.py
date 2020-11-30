from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightPauseMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6766
        self.isPaused = {"type": "Boolean", "value": ""}
