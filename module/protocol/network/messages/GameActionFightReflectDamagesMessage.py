from module.protocol.network.message import Message


class GameActionFightReflectDamagesMessage(Message):
    def __init__(self):
        self.id = 3447
