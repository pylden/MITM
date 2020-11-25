from module.protocol.network.message import Message


class GameActionFightInvisibleDetectedMessage(Message):
    def __init__(self):
        self.id = 2560
