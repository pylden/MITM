from module.protocol.network.message import Message


class PrismSetSabotagedRequestMessage(Message):
    def __init__(self):
        self.id = 9154
