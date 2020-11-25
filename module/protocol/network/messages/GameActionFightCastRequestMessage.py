from module.protocol.network.message import Message


class GameActionFightCastRequestMessage(Message):
    def __init__(self):
        self.id = 8507
