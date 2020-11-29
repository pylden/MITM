from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceFactsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9721
        self.vars.append({"name": "infos", "type": "AllianceFactSheetInformations", "value": ""})
        self.vars.append({"name": "guilds", "type": "Vector.<GuildInAllianceInformations>", "value": ""})
        self.vars.append({"name": "controlledSubareaIds", "type": "Vector.<uint>", "value": ""})
        self.vars.append({"name": "leaderCharacterId", "type": "Number", "value": ""})
        self.vars.append({"name": "leaderCharacterName", "type": "String", "value": ""})
