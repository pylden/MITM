from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildInvitationAnswerMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8465
        self.vars.append({"name": "accept", "type": "Boolean", "value": ""})
