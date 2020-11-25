from module.protocol.network.message import Message


class LockableChangeCodeMessage(Message):
    def __init__(self):
        self.id = 7253
        self.code = {"type": "String", "value": ""}
