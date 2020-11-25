from module.protocol.network.message import Message


class PrismUseRequestMessage(Message):
    def __init__(self):
        self.id = 6760
