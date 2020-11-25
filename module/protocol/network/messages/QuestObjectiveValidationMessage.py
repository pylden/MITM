from module.protocol.network.message import Message


class QuestObjectiveValidationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8867
        self.questId = {"type": "uint", "value": ""}
        self.objectiveId = {"type": "uint", "value": ""}
