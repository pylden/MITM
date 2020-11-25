from module.protocol.network.message import Message


class PrismsListRegisterMessage(Message):
    def __init__(self):
        self.id = 9690
