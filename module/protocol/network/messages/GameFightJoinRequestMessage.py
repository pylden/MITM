from module.protocol.network.message import Message


class GameFightJoinRequestMessage(Message):
    def __init__(self):
        self.id = 3211
