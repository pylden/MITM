from module.protocol.network.message import Message


class SequenceStartMessage(Message):
    def __init__(self):
        self.id = 9373
