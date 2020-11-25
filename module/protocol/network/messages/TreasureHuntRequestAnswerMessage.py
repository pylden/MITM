from module.protocol.network.message import Message


class TreasureHuntRequestAnswerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6525
        self.questType = {"type": "uint", "value": ""}
        self.result = {"type": "uint", "value": ""}
