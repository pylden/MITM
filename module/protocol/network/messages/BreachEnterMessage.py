from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachEnterMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3176
        self.owner = {"type": "Number", "value": ""}
