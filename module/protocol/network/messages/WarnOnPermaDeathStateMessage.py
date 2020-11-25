from module.protocol.network.message import Message


class WarnOnPermaDeathStateMessage(Message):
    def __init__(self):
        self.id = 2119
