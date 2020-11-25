from module.protocol.network.message import Message


class SelectedServerDataMessage(Message):
    def __init__(self):
        self.id = 6182
        self.address = {"type": "String", "value": ""}
