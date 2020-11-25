from module.protocol.network.message import Message


class HaapiConfirmationRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3477
        self.kamas = {"type": "Number", "value": ""}
        self.ogrines = {"type": "Number", "value": ""}
        self.rate = {"type": "uint", "value": ""}
        self.action = {"type": "uint", "value": ""}
