from module.protocol.network.message import Message


class GameFightSynchronizeMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 276
        self.fighters = {"type": "Vector.<GameFightFighterInformations>", "value": ""}
