from module.protocol.network.message import Message


class HaapiBuyValidationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7568
        self.amount = {"type": "Number", "value": ""}
        self.email = {"type": "String", "value": ""}
