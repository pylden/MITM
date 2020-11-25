from module.protocol.network.message import Message


class StartupActionFinishedMessage(Message):
    def __init__(self):
        self.id = 3256
