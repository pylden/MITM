from module.protocol.network.message import Message


class QuestObjectiveValidatedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4838
        self.questId = {"type": "uint", "value": ""}
        self.objectiveId = {"type": "uint", "value": ""}
