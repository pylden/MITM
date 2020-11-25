from module.protocol.network.message import Message


class LifePointsRegenBeginMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1894
        self.regenRate = {"type": "uint", "value": ""}
