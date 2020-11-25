from module.protocol.network.message import Message


class BreachTeleportResponseMessage(Message):
    def __init__(self):
        self.id = 870
