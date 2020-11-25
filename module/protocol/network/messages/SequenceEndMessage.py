from module.protocol.network.message import Message


class SequenceEndMessage(Message):
    def __init__(self):
        self.id = 8673
