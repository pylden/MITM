from module.protocol.network.message import Message


class TaxCollectorMovementMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9446
        self.movementType = {"type": "uint", "value": ""}
        self.basicInfos = {"type": "TaxCollectorBasicInformations", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
        self.playerName = {"type": "String", "value": ""}
