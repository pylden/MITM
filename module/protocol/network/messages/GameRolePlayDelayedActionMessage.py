from module.protocol.network.message import Message


class GameRolePlayDelayedActionMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4027
        self.delayedCharacterId = {"type": "Number", "value": ""}
        self.delayTypeId = {"type": "uint", "value": ""}
        self.delayEndTime = {"type": "Number", "value": ""}
