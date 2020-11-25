from module.protocol.network.message import Message


class TaxCollectorStateUpdateMessage(Message):
    def __init__(self):
        self.id = 5755
