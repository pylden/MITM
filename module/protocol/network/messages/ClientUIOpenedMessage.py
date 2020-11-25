from module.protocol.network.message import Message


class ClientUIOpenedMessage(Message):
    def __init__(self):
        self.id = 1056
