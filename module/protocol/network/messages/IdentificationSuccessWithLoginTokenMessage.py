from module.protocol.network.message import Message


class IdentificationSuccessWithLoginTokenMessage(Message):
    def __init__(self):
        self.id = 5260
        self.loginToken = {"type": "String", "value": ""}
