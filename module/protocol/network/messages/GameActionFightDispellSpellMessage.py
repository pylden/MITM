from module.protocol.network.message import Message


class GameActionFightDispellSpellMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4229
        self.spellId = {"type": "uint", "value": ""}
