from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachRewardBuyMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 680
        self.id = {"type": "uint", "value": ""}
