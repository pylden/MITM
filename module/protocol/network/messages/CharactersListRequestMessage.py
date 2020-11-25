from module.protocol.network.message import Message


class CharactersListRequestMessage(Message):
    def __init__(self):
        self.id = 3340
