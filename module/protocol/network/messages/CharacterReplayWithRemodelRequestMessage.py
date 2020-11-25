from module.protocol.network.message import Message


class CharacterReplayWithRemodelRequestMessage(Message):
    def __init__(self):
        self.id = 9190
