from module.protocol.network.message import Message


class QuestStartedMessage(Message):
    def __init__(self):
        self.id = 5033
