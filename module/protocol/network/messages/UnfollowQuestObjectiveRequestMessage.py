from module.protocol.network.message import Message


class UnfollowQuestObjectiveRequestMessage(Message):
    def __init__(self):
        self.id = 5582
