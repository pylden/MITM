from module.protocol.network.message import Message


class GoldAddedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1942
        self.gold = {"type": "GoldItem", "value": ""}
