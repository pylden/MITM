from module.protocol.network.message import Message


class QuestStepInfoRequestMessage(Message):
    def __init__(self):
        self.id = 3636
