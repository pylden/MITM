from module.protocol.network.message import Message


class FollowQuestObjectiveRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7841
        self.questId = {"type": "uint", "value": ""}
        self.objectiveId = {"type": "int", "value": ""}
