from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceModificationValidMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8871
        self.vars.append({"name": "allianceName", "type": "String", "value": ""})
        self.vars.append({"name": "allianceTag", "type": "String", "value": ""})
        self.vars.append({"name": "Alliancemblem", "type": "GuildEmblem", "value": ""})
