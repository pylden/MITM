from module.protocol.network.message import Message


class AllianceMotdSetRequestMessage(Message):
    def __init__(self):
        self.id = 6658
        self.content = {"type": "String", "value": ""}
