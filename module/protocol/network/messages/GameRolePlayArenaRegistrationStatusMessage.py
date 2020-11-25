from module.protocol.network.message import Message


class GameRolePlayArenaRegistrationStatusMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2867
        self.registered = {"type": "Boolean", "value": ""}
        self.step = {"type": "uint", "value": ""}
        self.battleMode = {"type": "uint", "value": ""}
