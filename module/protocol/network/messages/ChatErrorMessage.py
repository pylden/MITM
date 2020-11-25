from module.protocol.network.message import Message


class ChatErrorMessage(Message):
    def __init__(self):
        self.id = 5057
