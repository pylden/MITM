from module.protocol.network.message import Message


class TreasureHuntFinishedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4291
        self.questType = {"type": "uint", "value": ""}
