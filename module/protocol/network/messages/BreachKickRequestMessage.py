from module.protocol.network.message import Message


class BreachKickRequestMessage(Message):
    def __init__(self):
        self.id = 8280
