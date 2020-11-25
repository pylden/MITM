from module.protocol.network.message import Message


class IdentificationSuccessMessage(Message):
    def __init__(self):
        self.id = 8394
        self.login = {"type": "String", "value": ""}
        self.nickname = {"type": "String", "value": ""}
        self.secretQuestion = {"type": "String", "value": ""}
