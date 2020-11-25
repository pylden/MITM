from module.protocol.network.message import Message


class GameActionFightReduceDamagesMessage(Message):
    def __init__(self):
        self.id = 3507
