from module.protocol.network.message import Message


class IdentificationSuccessWithLoginTokenMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5260
        self.loginToken = {"type": "String", "value": ""}
