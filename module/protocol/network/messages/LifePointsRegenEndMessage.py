from module.protocol.network.message import Message


class LifePointsRegenEndMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3437
        self.lifePointsGained = {"type": "uint", "value": ""}
