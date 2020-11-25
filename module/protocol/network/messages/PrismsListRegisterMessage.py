from module.protocol.network.message import Message


class PrismsListRegisterMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9690
        self.listen = {"type": "uint", "value": ""}
