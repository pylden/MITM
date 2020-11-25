from module.protocol.network.message import Message


class GameFightResumeMessage(Message):
    def __init__(self):
        self.id = 7999
