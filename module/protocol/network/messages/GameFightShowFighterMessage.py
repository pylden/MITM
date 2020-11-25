from module.protocol.network.message import Message


class GameFightShowFighterMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9957
        self.informations = {"type": "GameFightFighterInformations", "value": ""}
