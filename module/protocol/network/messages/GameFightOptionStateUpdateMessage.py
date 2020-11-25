from module.protocol.network.message import Message


class GameFightOptionStateUpdateMessage(Message):
    def __init__(self):
        self.id = 4253
