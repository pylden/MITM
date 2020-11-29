from module.protocol.network.messages.NetworkMessage import NetworkMessage


class KohUpdateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6840
        self.vars.append({"name": "alliances", "type": "Vector.<AllianceInformations>", "value": ""})
        self.vars.append({"name": "allianceNbMembers", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "allianceRoundWeigth", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "allianceMatchScore", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "allianceMapWinners", "type": "Vector.<BasicAllianceInformations>", "value": ""})
        self.vars.append({"name": "allianceMapWinnerScore", "type": "uint", "value": ""})
        self.vars.append({"name": "allianceMapMyAllianceScore", "type": "uint", "value": ""})
        self.vars.append({"name": "nextTickTime", "type": "Number", "value": ""})
