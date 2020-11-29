from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceCreationValidMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8739
        self.vars.append({"name": "allianceName", "type": "String", "value": ""})
        self.vars.append({"name": "allianceTag", "type": "String", "value": ""})
        self.vars.append({"name": "allianceEmblem", "type": "GuildEmblem", "value": ""})
