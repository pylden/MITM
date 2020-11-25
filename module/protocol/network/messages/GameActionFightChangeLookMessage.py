from module.protocol.network.message import Message


class GameActionFightChangeLookMessage(Message):
    def __init__(self):
        self.id = 3680
