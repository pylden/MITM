from module.protocol.network.message import Message


class TreasureHuntFlagRemoveRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7652
        self.questType = {"type": "uint", "value": ""}
        self.index = {"type": "uint", "value": ""}
