from module.protocol.network.message import Message


class DungeonPartyFinderListenRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6729
        self.dungeonId = {"type": "uint", "value": ""}
