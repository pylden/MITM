from module.protocol.network.message import Message


class IdentificationSuccessMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8394
        self.login = {"type": "String", "value": ""}
        self.nickname = {"type": "String", "value": ""}
        self.secretQuestion = {"type": "String", "value": ""}
