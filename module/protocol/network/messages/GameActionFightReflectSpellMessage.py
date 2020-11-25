from module.protocol.network.message import Message


class GameActionFightReflectSpellMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7706
        self.targetId = {"type": "Number", "value": ""}
