from module.protocol.network.message import Message


class QuestStartedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5033
        self.questId = {"type": "uint", "value": ""}
