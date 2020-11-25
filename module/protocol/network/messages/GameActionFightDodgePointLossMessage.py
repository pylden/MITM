from module.protocol.network.message import Message


class GameActionFightDodgePointLossMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9316
        self.targetId = {"type": "Number", "value": ""}
        self.amount = {"type": "uint", "value": ""}
