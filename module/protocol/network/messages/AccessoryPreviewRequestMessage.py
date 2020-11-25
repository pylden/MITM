from module.protocol.network.message import Message


class AccessoryPreviewRequestMessage(Message):
    def __init__(self):
        self.id = 9763
