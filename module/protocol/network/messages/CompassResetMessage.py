from module.protocol.network.message import Message


class CompassResetMessage(Message):
    def __init__(self):
        self.id = 2894
