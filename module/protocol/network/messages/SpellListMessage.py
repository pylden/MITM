from module.protocol.network.message import Message


class SpellListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6326
        self.spellPrevisualization = {"type": "Boolean", "value": ""}
        self.spells = {"type": "Vector.<SpellItem>", "value": ""}
