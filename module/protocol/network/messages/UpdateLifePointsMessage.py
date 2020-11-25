from module.protocol.network.message import Message


class UpdateLifePointsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8175
        self.lifePoints = {"type": "uint", "value": ""}
        self.maxLifePoints = {"type": "uint", "value": ""}
