from module.protocol.network.message import Message


class TaxCollectorMovementRemoveMessage(Message):
    def __init__(self):
        self.id = 6992
