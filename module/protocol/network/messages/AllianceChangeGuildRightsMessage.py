from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceChangeGuildRightsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8726
        self.guildId = {"type": "uint", "value": ""}
        self.rights = {"type": "uint", "value": ""}
