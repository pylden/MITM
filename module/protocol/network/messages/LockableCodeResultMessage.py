from module.protocol.network.message import Message


class LockableCodeResultMessage(Message):
    def __init__(self):
        self.id = 302
