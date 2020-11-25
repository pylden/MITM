from module.protocol.network.message import Message


class AbstractPartyEventMessage(Message):
    def __init__(self):
        self.id = 5971
