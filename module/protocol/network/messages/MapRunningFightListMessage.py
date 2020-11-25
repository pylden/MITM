from module.protocol.network.message import Message


class MapRunningFightListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3292
        self.fights = {"type": "Vector.<FightExternalInformations>", "value": ""}
