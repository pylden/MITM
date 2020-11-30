from module.protocol.network.messages.GameFightResumeMessage import GameFightResumeMessage


class GameFightResumeWithSlavesMessage(GameFightResumeMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameFightResumeMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1238
        self.slavesInfo = {"type": "Vector.<GameFightResumeSlaveInfo>", "value": ""}
