from module.protocol.network.message import Message


class FinishMoveListRequestMessage(Message):
    def __init__(self):
        self.id = 6971
