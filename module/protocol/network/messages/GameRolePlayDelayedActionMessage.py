from module.protocol.network.message import Message


class GameRolePlayDelayedActionMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4027
        self.delayedCharacterId = {"type": "Number", "value": ""}
        self.delayTypeId = {"type": "uint", "value": ""}
        self.delayEndTime = {"type": "Number", "value": ""}
