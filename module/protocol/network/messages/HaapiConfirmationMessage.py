from module.protocol.network.message import Message


class HaapiConfirmationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7797
        self.kamas = {"type": "Number", "value": ""}
        self.amount = {"type": "Number", "value": ""}
        self.rate = {"type": "uint", "value": ""}
        self.action = {"type": "uint", "value": ""}
        self.transaction = {"type": "String", "value": ""}
