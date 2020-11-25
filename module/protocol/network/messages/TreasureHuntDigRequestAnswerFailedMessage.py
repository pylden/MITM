from module.protocol.network.message import Message


class TreasureHuntDigRequestAnswerFailedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5389
        self.wrongFlagCount = {"type": "uint", "value": ""}
