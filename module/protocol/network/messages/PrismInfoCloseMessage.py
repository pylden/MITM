from module.protocol.network.message import Message


class PrismInfoCloseMessage(Message):
    def __init__(self):
        self.id = 496
