from module.protocol.network.message import Message


class BreachRoomLockedMessage(Message):
    def __init__(self):
        self.id = 3599
