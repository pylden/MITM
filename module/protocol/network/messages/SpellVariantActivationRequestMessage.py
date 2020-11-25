from module.protocol.network.message import Message


class SpellVariantActivationRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9900
        self.spellId = {"type": "uint", "value": ""}
