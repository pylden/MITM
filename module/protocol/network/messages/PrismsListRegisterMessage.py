from module.protocol.network.message import Message


class PrismsListRegisterMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9690
        self.listen = {"type": "uint", "value": ""}
