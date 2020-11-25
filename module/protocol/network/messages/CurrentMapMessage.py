from module.protocol.network.message import Message


class CurrentMapMessage(Message):
    def __init__(self):
        self.id = 7422
        self.mapKey = {"type": "String", "value": ""}
