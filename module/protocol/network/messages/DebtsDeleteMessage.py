from module.protocol.network.message import Message


class DebtsDeleteMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 190
        self.reason = {"type": "uint", "value": ""}
        self.debts = {"type": "Vector.<Number>", "value": ""}
