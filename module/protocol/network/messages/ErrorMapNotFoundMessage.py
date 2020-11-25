from module.protocol.network.message import Message


class ErrorMapNotFoundMessage(Message):
    def __init__(self):
        self.id = 8048
