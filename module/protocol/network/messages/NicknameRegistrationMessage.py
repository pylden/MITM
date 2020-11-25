from module.protocol.network.message import Message


class NicknameRegistrationMessage(Message):
    def __init__(self):
        self.id = 3860
