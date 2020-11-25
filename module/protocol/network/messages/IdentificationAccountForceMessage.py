from module.protocol.network.message import Message


class IdentificationAccountForceMessage(Message):
    def __init__(self):
        self.id = 4388
        self.forcedAccountLogin = {"type": "String", "value": ""}
