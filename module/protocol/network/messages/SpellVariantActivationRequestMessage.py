from module.protocol.network.message import Message


class SpellVariantActivationRequestMessage(Message):
    def __init__(self):
        self.id = 9900
