from module.protocol.network.messages.GuildFactsMessage import GuildFactsMessage


class GuildInAllianceFactsMessage(GuildFactsMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GuildFactsMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3384
        self.allianceInfos = {"type": "BasicNamedAllianceInformations", "value": ""}
