from module.protocol.network.message import Message


class HaapiCancelBidRequestMessage(Message):
    def __init__(self):
        self.id = 9408
