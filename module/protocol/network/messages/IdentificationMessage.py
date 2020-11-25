from module.protocol.network.message import Message


class IdentificationMessage(Message):
    def __init__(self):
        self.id = 5833
        self.lang = {"type": "String", "value": ""}
