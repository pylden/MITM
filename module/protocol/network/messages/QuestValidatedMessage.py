from module.protocol.network.message import Message


class QuestValidatedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5469
        self.questId = {"type": "uint", "value": ""}
