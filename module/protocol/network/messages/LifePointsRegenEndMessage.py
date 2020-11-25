from module.protocol.network.message import Message


class LifePointsRegenEndMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3437
        self.lifePointsGained = {"type": "uint", "value": ""}
