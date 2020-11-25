from module.protocol.network.message import Message


class StopToListenRunningFightRequestMessage(Message):
    def __init__(self):
        self.id = 7620
