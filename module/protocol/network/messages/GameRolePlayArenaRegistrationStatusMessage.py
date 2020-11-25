from module.protocol.network.message import Message


class GameRolePlayArenaRegistrationStatusMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2867
        self.registered = {"type": "Boolean", "value": ""}
        self.step = {"type": "uint", "value": ""}
        self.battleMode = {"type": "uint", "value": ""}
