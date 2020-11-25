from module.protocol.network.message import Message


class CharacterSelectedErrorMessage(Message):
    def __init__(self):
        self.id = 5817
