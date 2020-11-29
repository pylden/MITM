from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceModificationEmblemValidMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2632
        self.vars.append({"name": "Alliancemblem", "type": "GuildEmblem", "value": ""})
