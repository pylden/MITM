from module.protocol.network.message import Message


class TitleLostMessage(Message):
    def __init__(self):
        self.id = 9752
