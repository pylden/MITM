from module.protocol.network.message import Message


class CharactersListErrorMessage(Message):
    def __init__(self):
        self.id = 7577
