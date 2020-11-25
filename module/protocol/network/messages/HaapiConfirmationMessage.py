from module.protocol.network.message import Message


class HaapiConfirmationMessage(Message):
    def __init__(self):
        self.id = 7797
        self.transaction = {"type": "String", "value": ""}
