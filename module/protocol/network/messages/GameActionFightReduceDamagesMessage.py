from module.protocol.network.message import Message


class GameActionFightReduceDamagesMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3507
        self.targetId = {"type": "Number", "value": ""}
        self.amount = {"type": "uint", "value": ""}
