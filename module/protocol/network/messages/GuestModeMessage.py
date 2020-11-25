from module.protocol.network.message import Message


class GuestModeMessage(Message):
    def __init__(self):
        self.id = 3850
