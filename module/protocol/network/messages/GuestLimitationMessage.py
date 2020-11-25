from module.protocol.network.message import Message


class GuestLimitationMessage(Message):
    def __init__(self):
        self.id = 2462
