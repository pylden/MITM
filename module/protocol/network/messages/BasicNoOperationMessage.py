from module.protocol.network.message import Message


class BasicNoOperationMessage(Message):
    def __init__(self):
        self.id = 1111
