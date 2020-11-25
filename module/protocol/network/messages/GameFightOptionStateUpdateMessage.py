from module.protocol.network.message import Message


class GameFightOptionStateUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4253
        self.fightId = {"type": "uint", "value": ""}
        self.teamId = {"type": "uint", "value": ""}
        self.option = {"type": "uint", "value": ""}
        self.state = {"type": "Boolean", "value": ""}
