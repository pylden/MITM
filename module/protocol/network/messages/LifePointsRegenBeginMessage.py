from module.protocol.network.messages.NetworkMessage import NetworkMessage


class LifePointsRegenBeginMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1894
        self.vars.append({"name": "regenRate", "type": "uint", "value": ""})
