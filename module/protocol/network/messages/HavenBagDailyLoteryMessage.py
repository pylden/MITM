from module.protocol.network.messages.NetworkMessage import NetworkMessage


class HavenBagDailyLoteryMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9224
        self.vars.append({"name": "returnType", "type": "uint", "value": ""})
        self.vars.append({"name": "gameActionId", "type": "String", "value": ""})
