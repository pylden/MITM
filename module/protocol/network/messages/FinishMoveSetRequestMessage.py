from module.protocol.network.message import Message


class FinishMoveSetRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8541
        self.finishMoveId = {"type": "uint", "value": ""}
        self.finishMoveState = {"type": "Boolean", "value": ""}
