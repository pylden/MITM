from module.protocol.network.message import Message


class GameActionNoopMessage(Message):
    def __init__(self):
        self.id = 5520
