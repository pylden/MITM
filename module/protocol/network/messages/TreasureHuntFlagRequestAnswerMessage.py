from module.protocol.network.message import Message


class TreasureHuntFlagRequestAnswerMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8358
        self.questType = {"type": "uint", "value": ""}
        self.result = {"type": "uint", "value": ""}
        self.index = {"type": "uint", "value": ""}
