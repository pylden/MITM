from module.protocol.network.message import Message


class AbstractPartyMessage(Message):
    def __init__(self):
        self.id = 555
