from module.protocol.network.message import Message


class QuestStepStartedMessage(Message):
    def __init__(self):
        self.id = 2982
