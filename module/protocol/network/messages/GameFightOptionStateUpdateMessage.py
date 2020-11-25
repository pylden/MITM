from module.protocol.network.message import Message


class GameFightOptionStateUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4253
        self.fightId = {"type": "uint", "value": ""}
        self.teamId = {"type": "uint", "value": ""}
        self.option = {"type": "uint", "value": ""}
        self.state = {"type": "Boolean", "value": ""}
