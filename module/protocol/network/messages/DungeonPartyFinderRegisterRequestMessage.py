from module.protocol.network.message import Message


class DungeonPartyFinderRegisterRequestMessage(Message):
    def __init__(self):
        self.id = 919
