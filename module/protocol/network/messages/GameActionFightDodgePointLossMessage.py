from module.protocol.network.message import Message


class GameActionFightDodgePointLossMessage(Message):
    def __init__(self):
        self.id = 9316
