from module.protocol.network.message import Message


class AllianceFactsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9721
        self.infos = {"type": "AllianceFactSheetInformations", "value": ""}
        self.guilds = {"type": "Vector.<GuildInAllianceInformations>", "value": ""}
        self.controlledSubareaIds = {"type": "Vector.<uint>", "value": ""}
        self.leaderCharacterId = {"type": "Number", "value": ""}
        self.leaderCharacterName = {"type": "String", "value": ""}
