from module.protocol.network.message import Message


class BreachTeleportRequestMessage(Message):
    def __init__(self):
        self.id = 9008
