from module.protocol.network.message import Message


class KohUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6840
        self.alliances = {"type": "Vector.<AllianceInformations>", "value": ""}
        self.allianceNbMembers = {"type": "Vector.<uint>", "value": ""}
        self.allianceRoundWeigth = {"type": "Vector.<uint>", "value": ""}
        self.allianceMatchScore = {"type": "Vector.<uint>", "value": ""}
        self.allianceMapWinners = {"type": "Vector.<BasicAllianceInformations>", "value": ""}
        self.allianceMapWinnerScore = {"type": "uint", "value": ""}
        self.allianceMapMyAllianceScore = {"type": "uint", "value": ""}
        self.nextTickTime = {"type": "Number", "value": ""}
