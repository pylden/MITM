from module.protocol.network.message import Message


class QuestValidatedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5469
        self.questId = {"type": "uint", "value": ""}
