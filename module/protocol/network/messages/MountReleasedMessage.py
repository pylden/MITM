from module.protocol.network.message import Message


class MountReleasedMessage(Message):
    def __init__(self):
        self.id = 3002
