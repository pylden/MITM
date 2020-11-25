from module.protocol.network.message import Message


class IdentificationAccountForceMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4388
        self.forcedAccountLogin = {"type": "String", "value": ""}
