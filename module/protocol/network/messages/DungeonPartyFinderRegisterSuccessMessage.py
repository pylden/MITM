from module.protocol.network.message import Message


class DungeonPartyFinderRegisterSuccessMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9170
        self.dungeonIds = {"type": "Vector.<uint>", "value": ""}
