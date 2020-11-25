from module.protocol.network.message import Message


class DebtsDeleteMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 190
        self.reason = {"type": "uint", "value": ""}
        self.debts = {"type": "Vector.<Number>", "value": ""}
