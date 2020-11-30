from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceFactsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9721
        self.infos = {"type": "AllianceFactSheetInformations", "value": ""}
        self.guilds = {"type": "Vector.<GuildInAllianceInformations>", "value": ""}
        self.controlledSubareaIds = {"type": "Vector.<uint>", "value": ""}
        self.leaderCharacterId = {"type": "Number", "value": ""}
        self.leaderCharacterName = {"type": "String", "value": ""}
