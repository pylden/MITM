from module.protocol.network.message import Message


class TreasureHuntFlagRequestAnswerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8358
        self.questType = {"type": "uint", "value": ""}
        self.result = {"type": "uint", "value": ""}
        self.index = {"type": "uint", "value": ""}
