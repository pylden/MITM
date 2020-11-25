from module.protocol.network.message import Message


class TreasureHuntDigRequestAnswerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7127
        self.questType = {"type": "uint", "value": ""}
        self.result = {"type": "uint", "value": ""}
