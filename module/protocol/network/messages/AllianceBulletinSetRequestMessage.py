from module.protocol.network.message import Message


class AllianceBulletinSetRequestMessage(Message):
    def __init__(self):
        self.id = 8756
        self.content = {"type": "String", "value": ""}
