from module.protocol.network.message import Message


class MountReleaseRequestMessage(Message):
    def __init__(self):
        self.id = 9401
