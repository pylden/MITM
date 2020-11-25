from module.protocol.network.message import Message


class LockableStateUpdateAbstractMessage(Message):
    def __init__(self):
        self.id = 4237
