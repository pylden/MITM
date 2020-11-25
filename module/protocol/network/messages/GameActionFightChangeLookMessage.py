from module.protocol.network.message import Message


class GameActionFightChangeLookMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3680
        self.targetId = {"type": "Number", "value": ""}
        self.entityLook = {"type": "EntityLook", "value": ""}
