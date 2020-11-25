from module.protocol.network.message import Message


class IdentificationSuccessWithLoginTokenMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5260
        self.loginToken = {"type": "String", "value": ""}
