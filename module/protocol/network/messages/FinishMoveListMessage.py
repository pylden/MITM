from module.protocol.network.message import Message


class FinishMoveListMessage(Message):
    def __init__(self):
        self.id = 6941
