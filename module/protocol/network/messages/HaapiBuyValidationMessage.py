from module.protocol.network.message import Message


class HaapiBuyValidationMessage(Message):
    def __init__(self):
        self.id = 7568
        self.email = {"type": "String", "value": ""}
