from module.protocol.network.message import Message


class FinishMoveSetRequestMessage(Message):
    def __init__(self):
        self.id = 8541
