from module.protocol.network.message import Message


class MountSetXpRatioRequestMessage(Message):
    def __init__(self):
        self.id = 4309
