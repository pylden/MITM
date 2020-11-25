from module.protocol.network.message import Message


class QuestStepStartedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2982
        self.questId = {"type": "uint", "value": ""}
        self.stepId = {"type": "uint", "value": ""}
