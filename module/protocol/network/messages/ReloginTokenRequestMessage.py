from module.protocol.network.message import Message


class ReloginTokenRequestMessage(Message):
    def __init__(self):
        self.id = 8552
