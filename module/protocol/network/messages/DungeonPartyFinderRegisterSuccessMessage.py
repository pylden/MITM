from module.protocol.network.message import Message


class DungeonPartyFinderRegisterSuccessMessage(Message):
    def __init__(self):
        self.id = 9170
