from module.protocol.network.message import Message


class GoldAddedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1942
        self.gold = {"type": "GoldItem", "value": ""}
