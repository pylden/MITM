from module.protocol.network.message import Message


class GameRolePlayPlayerFightRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8916
        self.targetId = {"type": "Number", "value": ""}
        self.targetCellId = {"type": "int", "value": ""}
        self.friendly = {"type": "Boolean", "value": ""}
