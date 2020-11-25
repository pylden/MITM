from module.protocol.network.message import Message


class GameFightSynchronizeMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 276
        self.fighters = {"type": "Vector.<GameFightFighterInformations>", "value": ""}
