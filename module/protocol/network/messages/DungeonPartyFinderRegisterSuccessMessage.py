from module.protocol.network.message import Message


class DungeonPartyFinderRegisterSuccessMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9170
        self.dungeonIds = {"type": "Vector.<uint>", "value": ""}
