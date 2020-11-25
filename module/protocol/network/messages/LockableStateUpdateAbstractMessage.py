from module.protocol.network.message import Message


class LockableStateUpdateAbstractMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4237
        self.locked = {"type": "Boolean", "value": ""}
