from module.protocol.network.message import Message


class GameActionFightSummonMessage(Message):
    def __init__(self):
        self.id = 2182
