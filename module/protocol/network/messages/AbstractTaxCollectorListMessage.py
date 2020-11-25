from module.protocol.network.message import Message


class AbstractTaxCollectorListMessage(Message):
    def __init__(self):
        self.id = 4914
