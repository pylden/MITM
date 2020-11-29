from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AchievementDetailedListRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7504
        self.vars.append({"name": "categoryId", "type": "uint", "value": ""})
