from module.protocol.network.message import Message


class TaxCollectorAttackedResultMessage(Message):
    def __init__(self):
        self.id = 8211
