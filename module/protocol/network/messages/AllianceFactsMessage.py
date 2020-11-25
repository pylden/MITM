from module.protocol.network.message import Message


class AllianceFactsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9721
        self.infos = {"type": "AllianceFactSheetInformations", "value": ""}
        self.guilds = {"type": "Vector.<GuildInAllianceInformations>", "value": ""}
        self.controlledSubareaIds = {"type": "Vector.<uint>", "value": ""}
        self.leaderCharacterId = {"type": "Number", "value": ""}
        self.leaderCharacterName = {"type": "String", "value": ""}
