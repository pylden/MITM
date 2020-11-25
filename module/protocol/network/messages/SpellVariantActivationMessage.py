from module.protocol.network.message import Message


class SpellVariantActivationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8938
        self.spellId = {"type": "uint", "value": ""}
        self.result = {"type": "Boolean", "value": ""}
