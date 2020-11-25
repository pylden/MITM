from module.protocol.network.message import Message


class PrismSetSabotagedRefusedMessage(Message):
    def __init__(self):
        self.id = 1834
