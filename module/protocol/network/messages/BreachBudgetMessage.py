from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachBudgetMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6408
        self.bugdet = {"type": "uint", "value": ""}
