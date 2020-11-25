from module.protocol.network.message import Message


class UpdateLifePointsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8175
        self.lifePoints = {"type": "uint", "value": ""}
        self.maxLifePoints = {"type": "uint", "value": ""}
