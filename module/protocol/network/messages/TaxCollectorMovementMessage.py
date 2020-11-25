from module.protocol.network.message import Message


class TaxCollectorMovementMessage(Message):
    def __init__(self):
        self.id = 9446
        self.playerName = {"type": "String", "value": ""}
