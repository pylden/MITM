from module.protocol.network.message import Message


class GameFightResumeWithSlavesMessage(Message):
    def __init__(self):
        self.id = 1238
