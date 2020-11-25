from module.protocol.network.message import Message


class GameRolePlayPlayerFightRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8916
        self.targetId = {"type": "Number", "value": ""}
        self.targetCellId = {"type": "int", "value": ""}
        self.friendly = {"type": "Boolean", "value": ""}
