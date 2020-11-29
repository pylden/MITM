from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceInsiderInfoMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4742
        self.vars.append({"name": "allianceInfos", "type": "AllianceFactSheetInformations", "value": ""})
        self.vars.append({"name": "guilds", "type": "Vector.<GuildInsiderFactSheetInformations>", "value": ""})
        self.vars.append({"name": "prisms", "type": "Vector.<PrismSubareaEmptyInfo>", "value": ""})
