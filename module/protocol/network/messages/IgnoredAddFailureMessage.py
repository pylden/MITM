from module.protocol.network.message import Message


class IgnoredAddFailureMessage(Message):
    def __init__(self):
        self.id = 9626
