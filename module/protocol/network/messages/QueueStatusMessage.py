from module.protocol.network.message import Message


class QueueStatusMessage(Message):
    def __init__(self):
        self.id = 9955
