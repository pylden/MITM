from module.protocol.network.message import Message


class TeleportOnSameMapMessage(Message):
    def __init__(self):
        self.id = 7423
