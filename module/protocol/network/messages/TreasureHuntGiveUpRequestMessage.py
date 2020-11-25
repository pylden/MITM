from module.protocol.network.message import Message


class TreasureHuntGiveUpRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1127
        self.questType = {"type": "uint", "value": ""}
