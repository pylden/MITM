from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildInvitedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3856
        self.vars.append({"name": "recruterId", "type": "Number", "value": ""})
        self.vars.append({"name": "recruterName", "type": "String", "value": ""})
        self.vars.append({"name": "guildInfo", "type": "BasicGuildInformations", "value": ""})
