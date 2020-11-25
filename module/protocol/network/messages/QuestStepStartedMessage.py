from module.protocol.network.message import Message


class QuestStepStartedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2982
        self.questId = {"type": "uint", "value": ""}
        self.stepId = {"type": "uint", "value": ""}
