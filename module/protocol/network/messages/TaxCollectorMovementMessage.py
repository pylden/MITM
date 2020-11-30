from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TaxCollectorMovementMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9446
        self.movementType = {"type": "uint", "value": ""}
        self.basicInfos = {"type": "TaxCollectorBasicInformations", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
        self.playerName = {"type": "String", "value": ""}
