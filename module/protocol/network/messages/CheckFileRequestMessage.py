from module.protocol.network.message import Message


class CheckFileRequestMessage(Message):
    def __init__(self):
        self.id = 4509
        self.filename = {"type": "String", "value": ""}
