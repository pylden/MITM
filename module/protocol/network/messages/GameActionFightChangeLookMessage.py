from module.protocol.network.message import Message


class GameActionFightChangeLookMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3680
        self.targetId = {"type": "Number", "value": ""}
        self.entityLook = {"type": "EntityLook", "value": ""}
