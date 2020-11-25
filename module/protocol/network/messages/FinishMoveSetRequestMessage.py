from module.protocol.network.message import Message


class FinishMoveSetRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8541
        self.finishMoveId = {"type": "uint", "value": ""}
        self.finishMoveState = {"type": "Boolean", "value": ""}
