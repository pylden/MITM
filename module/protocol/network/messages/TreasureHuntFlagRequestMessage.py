from module.protocol.network.message import Message


class TreasureHuntFlagRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8451
        self.questType = {"type": "uint", "value": ""}
        self.index = {"type": "uint", "value": ""}
