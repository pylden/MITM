from module.protocol.network.message import Message


class TaxCollectorMovementMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9446
        self.movementType = {"type": "uint", "value": ""}
        self.basicInfos = {"type": "TaxCollectorBasicInformations", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
        self.playerName = {"type": "String", "value": ""}
