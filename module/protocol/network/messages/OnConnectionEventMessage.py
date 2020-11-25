from module.protocol.network.message import Message


class OnConnectionEventMessage(Message):
    def __init__(self):
        self.id = 2093
