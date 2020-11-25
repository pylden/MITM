from module.protocol.network.message import Message


class TreasureHuntDigRequestAnswerFailedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5389
        self.wrongFlagCount = {"type": "uint", "value": ""}
