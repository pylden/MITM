from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildInvitationMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6688
        self.vars.append({"name": "targetId", "type": "Number", "value": ""})
