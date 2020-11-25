from module.protocol.network.message import Message


class DebugInClientMessage(Message):
    def __init__(self):
        self.id = 1327
        self.message = {"type": "String", "value": ""}
