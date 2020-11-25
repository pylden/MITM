from module.protocol.network.message import Message


class MountDataErrorMessage(Message):
    def __init__(self):
        self.id = 9319
