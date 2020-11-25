from module.protocol.network.message import Message


class MapRunningFightListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3292
        self.fights = {"type": "Vector.<FightExternalInformations>", "value": ""}
