from module.protocol.network.message import Message


class GameActionFightCloseCombatMessage(Message):
    def __init__(self):
        self.id = 1677
