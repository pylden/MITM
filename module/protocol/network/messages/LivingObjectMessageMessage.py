from module.protocol.network.message import Message


class LivingObjectMessageMessage(Message):
    def __init__(self):
        self.id = 9436
        self.owner = {"type": "String", "value": ""}
