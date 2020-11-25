from module.protocol.network.message import Message


class AchievementFinishedInformationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7636
        self.name = {"type": "String", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
