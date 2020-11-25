from module.protocol.network.message import Message


class BasicPongMessage(Message):
    def __init__(self):
        self.id = 5053
