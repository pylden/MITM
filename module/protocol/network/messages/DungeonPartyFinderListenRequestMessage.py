from module.protocol.network.message import Message


class DungeonPartyFinderListenRequestMessage(Message):
    def __init__(self):
        self.id = 6729
