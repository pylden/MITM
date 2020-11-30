from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TeleportBuddiesAnswerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7598
        self.accept = {"type": "Boolean", "value": ""}
