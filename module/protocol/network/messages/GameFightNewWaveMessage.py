from module.protocol.network.message import Message


class GameFightNewWaveMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5791
        self.id = {"type": "uint", "value": ""}
        self.teamId = {"type": "uint", "value": ""}
        self.nbTurnBeforeNextWave = {"type": "int", "value": ""}
