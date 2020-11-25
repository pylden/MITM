from module.protocol.network.message import Message


class UpdateLifePointsMessage(Message):
    def __init__(self):
        self.id = 8175
