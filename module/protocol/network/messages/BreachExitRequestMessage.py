from module.protocol.network.message import Message


class BreachExitRequestMessage(Message):
    def __init__(self):
        self.id = 8694
