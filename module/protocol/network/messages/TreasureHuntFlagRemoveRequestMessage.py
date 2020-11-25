from module.protocol.network.message import Message


class TreasureHuntFlagRemoveRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7652
        self.questType = {"type": "uint", "value": ""}
        self.index = {"type": "uint", "value": ""}
