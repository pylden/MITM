from module.protocol.network.message import Message


class IdolSelectErrorMessage(Message):
    def __init__(self):
        self.id = 3869
