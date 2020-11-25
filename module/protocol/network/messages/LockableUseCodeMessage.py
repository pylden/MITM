from module.protocol.network.message import Message


class LockableUseCodeMessage(Message):
    def __init__(self):
        self.id = 632
        self.code = {"type": "String", "value": ""}
