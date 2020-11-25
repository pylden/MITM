from module.protocol.network.message import Message


class GameActionFightTackledMessage(Message):
    def __init__(self):
        self.id = 8815
