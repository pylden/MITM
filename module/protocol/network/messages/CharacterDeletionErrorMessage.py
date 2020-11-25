from module.protocol.network.message import Message


class CharacterDeletionErrorMessage(Message):
    def __init__(self):
        self.id = 6428
