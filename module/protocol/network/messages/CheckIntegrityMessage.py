from module.protocol.network.message import Message


class CheckIntegrityMessage(Message):
    def __init__(self):
        self.id = 8606
