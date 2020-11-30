from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachExitResponseMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 624
        self.exited = {"type": "Boolean", "value": ""}
