from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildKickRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2484
        self.vars.append({"name": "kickedId", "type": "Number", "value": ""})
