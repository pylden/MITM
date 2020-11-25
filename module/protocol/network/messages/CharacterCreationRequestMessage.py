from module.protocol.network.message import Message


class CharacterCreationRequestMessage(Message):
    def __init__(self):
        self.id = 1633
        self.name = {"type": "String", "value": ""}
