from module.protocol.network.message import Message


class GameActionFightReflectDamagesMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3447
        self.targetId = {"type": "Number", "value": ""}
