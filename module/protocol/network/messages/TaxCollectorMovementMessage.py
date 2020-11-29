from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TaxCollectorMovementMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9446
        self.vars.append({"name": "movementType", "type": "uint", "value": ""})
        self.vars.append({"name": "basicInfos", "type": "TaxCollectorBasicInformations", "value": ""})
        self.vars.append({"name": "playerId", "type": "Number", "value": ""})
        self.vars.append({"name": "playerName", "type": "String", "value": ""})
