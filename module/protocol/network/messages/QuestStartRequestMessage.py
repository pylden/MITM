from module.protocol.network.message import Message


class QuestStartRequestMessage(Message):
    def __init__(self):
        self.id = 823
