from module.protocol.network.message import Message


class NicknameChoiceRequestMessage(Message):
    def __init__(self):
        self.id = 5126
        self.nickname = {"type": "String", "value": ""}
