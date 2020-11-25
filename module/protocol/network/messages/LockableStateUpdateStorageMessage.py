from module.protocol.network.message import Message


class LockableStateUpdateStorageMessage(Message):
    def __init__(self):
        self.id = 2174
