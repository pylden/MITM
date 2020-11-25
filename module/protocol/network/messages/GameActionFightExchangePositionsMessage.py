from module.protocol.network.message import Message


class GameActionFightExchangePositionsMessage(Message):
    def __init__(self):
        self.id = 753
