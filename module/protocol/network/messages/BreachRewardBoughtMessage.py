from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachRewardBoughtMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 288
        self.id = {"type": "uint", "value": ""}
        self.bought = {"type": "Boolean", "value": ""}
