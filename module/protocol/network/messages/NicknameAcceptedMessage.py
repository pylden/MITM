from module.protocol.network.message import Message


class NicknameAcceptedMessage(Message):
    def __init__(self):
        self.id = 5508
