from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildInvitationByNameMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4298
        self.vars.append({"name": "name", "type": "String", "value": ""})
