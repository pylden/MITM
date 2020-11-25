from module.protocol.network.message import Message


class HaapiConfirmationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7797
        self.kamas = {"type": "Number", "value": ""}
        self.amount = {"type": "Number", "value": ""}
        self.rate = {"type": "uint", "value": ""}
        self.action = {"type": "uint", "value": ""}
        self.transaction = {"type": "String", "value": ""}
