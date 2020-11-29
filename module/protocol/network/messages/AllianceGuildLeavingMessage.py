from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AllianceGuildLeavingMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2611
        self.vars.append({"name": "kicked", "type": "Boolean", "value": ""})
        self.vars.append({"name": "guildId", "type": "uint", "value": ""})
