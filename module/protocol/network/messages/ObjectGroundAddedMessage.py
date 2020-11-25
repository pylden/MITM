from module.protocol.network.message import Message


class ObjectGroundAddedMessage(Message):
    def __init__(self):
        self.id = 8648
