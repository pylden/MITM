from module.protocol.network.message import Message


class KohUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6840
        self.alliances = {"type": "Vector.<AllianceInformations>", "value": ""}
        self.allianceNbMembers = {"type": "Vector.<uint>", "value": ""}
        self.allianceRoundWeigth = {"type": "Vector.<uint>", "value": ""}
        self.allianceMatchScore = {"type": "Vector.<uint>", "value": ""}
        self.allianceMapWinners = {"type": "Vector.<BasicAllianceInformations>", "value": ""}
        self.allianceMapWinnerScore = {"type": "uint", "value": ""}
        self.allianceMapMyAllianceScore = {"type": "uint", "value": ""}
        self.nextTickTime = {"type": "Number", "value": ""}
