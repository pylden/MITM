from module.protocol.network.message import Message


class AccessoryPreviewErrorMessage(Message):
    def __init__(self):
        self.id = 2799
