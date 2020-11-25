from module.protocol.network.message import Message


class GameActionFightReduceDamagesMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3507
        self.targetId = {"type": "Number", "value": ""}
        self.amount = {"type": "uint", "value": ""}
