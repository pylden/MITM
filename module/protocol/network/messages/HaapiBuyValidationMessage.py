from module.protocol.network.message import Message


class HaapiBuyValidationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7568
        self.amount = {"type": "Number", "value": ""}
        self.email = {"type": "String", "value": ""}
