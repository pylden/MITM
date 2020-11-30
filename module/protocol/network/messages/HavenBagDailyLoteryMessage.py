from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HavenBagDailyLoteryMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9224
        self.returnType = {"type": "uint", "value": ""}
        self.gameActionId = {"type": "String", "value": ""}
