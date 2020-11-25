from module.protocol.network.message import Message


class NicknameRefusedMessage(Message):
    def __init__(self):
        self.id = 4734
