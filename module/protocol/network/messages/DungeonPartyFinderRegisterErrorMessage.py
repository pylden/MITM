from module.protocol.network.message import Message


class DungeonPartyFinderRegisterErrorMessage(Message):
    def __init__(self):
        self.id = 9105
