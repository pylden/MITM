from module.protocol.network.message import Message


class DungeonPartyFinderAvailableDungeonsMessage(Message):
    def __init__(self):
        self.id = 1350
