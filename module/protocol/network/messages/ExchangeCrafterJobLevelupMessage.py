from module.protocol.network.message import Message


class ExchangeCrafterJobLevelupMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8633
        self.crafterJobLevel = {"type": "uint", "value": ""}
