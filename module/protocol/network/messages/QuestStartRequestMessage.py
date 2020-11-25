from module.protocol.network.message import Message


class QuestStartRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 823
        self.questId = {"type": "uint", "value": ""}
