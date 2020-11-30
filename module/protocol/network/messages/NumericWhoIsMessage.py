from module.protocol.network.messages.NetworkMessage import NetworkMessage


class NumericWhoIsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9545
        self.playerId = {"type": "Number", "value": ""}
        self.accountId = {"type": "uint", "value": ""}
