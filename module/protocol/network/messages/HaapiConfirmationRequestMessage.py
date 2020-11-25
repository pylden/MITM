from module.protocol.network.message import Message


class HaapiConfirmationRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3477
        self.kamas = {"type": "Number", "value": ""}
        self.ogrines = {"type": "Number", "value": ""}
        self.rate = {"type": "uint", "value": ""}
        self.action = {"type": "uint", "value": ""}
