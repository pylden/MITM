from module.protocol.network.message import Message


class DocumentReadingBeginMessage(Message):
    def __init__(self):
        self.id = 4915
