from module.protocol.network.message import Message


class DebtsUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3503
        self.action = {"type": "uint", "value": ""}
        self.debts = {"type": "Vector.<DebtInformation>", "value": ""}
