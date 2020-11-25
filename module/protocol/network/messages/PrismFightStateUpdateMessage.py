from module.protocol.network.message import Message


class PrismFightStateUpdateMessage(Message):
    def __init__(self):
        self.id = 1999
