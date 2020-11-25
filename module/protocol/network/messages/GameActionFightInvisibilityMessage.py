from module.protocol.network.message import Message


class GameActionFightInvisibilityMessage(Message):
    def __init__(self):
        self.id = 8056
