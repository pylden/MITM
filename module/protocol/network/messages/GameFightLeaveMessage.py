from module.protocol.network.message import Message


class GameFightLeaveMessage(Message):
    def __init__(self):
        self.id = 8271
