from module.protocol.network.message import Message


class QuestListRequestMessage(Message):
    def __init__(self):
        self.id = 5961
