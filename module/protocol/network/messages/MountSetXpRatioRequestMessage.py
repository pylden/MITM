from module.protocol.network.message import Message


class MountSetXpRatioRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4309
        self.xpRatio = {"type": "uint", "value": ""}
