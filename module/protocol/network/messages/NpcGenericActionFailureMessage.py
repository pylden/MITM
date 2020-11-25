from module.protocol.network.message import Message


class NpcGenericActionFailureMessage(Message):
    def __init__(self):
        self.id = 5321
