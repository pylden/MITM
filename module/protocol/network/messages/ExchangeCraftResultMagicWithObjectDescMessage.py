from module.protocol.network.message import Message


class ExchangeCraftResultMagicWithObjectDescMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 819
        self.magicPoolStatus = {"type": "int", "value": ""}
