from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AchievementDetailsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 360
        self.vars.append({"name": "achievement", "type": "Achievement", "value": ""})
