from module.protocol.network.message import Message


class BreachGameFightEndMessage(Message):
    def __init__(self):
        self.id = 4165
