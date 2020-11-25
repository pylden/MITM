from module.protocol.network.message import Message


class OrnamentLostMessage(Message):
    def __init__(self):
        self.id = 4335
