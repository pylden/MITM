from module.protocol.network.message import Message


class FollowQuestObjectiveRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7841
        self.questId = {"type": "uint", "value": ""}
        self.objectiveId = {"type": "int", "value": ""}
