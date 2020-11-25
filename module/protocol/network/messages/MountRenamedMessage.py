from module.protocol.network.message import Message


class MountRenamedMessage(Message):
    def __init__(self):
        self.id = 7458
        self.name = {"type": "String", "value": ""}
