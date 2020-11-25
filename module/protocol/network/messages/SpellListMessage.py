from module.protocol.network.message import Message


class SpellListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6326
        self.spellPrevisualization = {"type": "Boolean", "value": ""}
        self.spells = {"type": "Vector.<SpellItem>", "value": ""}
