from module.protocol.network.message import Message


class GameActionFightCastOnTargetRequestMessage(Message):
    def __init__(self):
        self.id = 1071
