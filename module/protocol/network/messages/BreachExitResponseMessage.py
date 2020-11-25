from module.protocol.network.message import Message


class BreachExitResponseMessage(Message):
    def __init__(self):
        self.id = 624
