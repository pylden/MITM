from module.protocol.network.message import Message


class AchievementDetailedListRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7504
        self.categoryId = {"type": "uint", "value": ""}
