from module.protocol.network.message import Message


class GameActionFightStealKamaMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7772
        self.targetId = {"type": "Number", "value": ""}
        self.amount = {"type": "Number", "value": ""}
