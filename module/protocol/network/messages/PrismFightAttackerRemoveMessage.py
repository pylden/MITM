from module.protocol.network.message import Message


class PrismFightAttackerRemoveMessage(Message):
    def __init__(self):
        self.id = 6001
