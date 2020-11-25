from module.protocol.network.message import Message


class SpellVariantActivationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8938
        self.spellId = {"type": "uint", "value": ""}
        self.result = {"type": "Boolean", "value": ""}
