from module.protocol.network.message import Message


class TitleSelectErrorMessage(Message):
    def __init__(self):
        self.id = 7192
