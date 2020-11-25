from module.protocol.network.message import Message


class TreasureHuntRequestAnswerMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6525
        self.questType = {"type": "uint", "value": ""}
        self.result = {"type": "uint", "value": ""}
