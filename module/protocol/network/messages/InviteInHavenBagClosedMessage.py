from module.protocol.network.messages.NetworkMessage import NetworkMessage


class InviteInHavenBagClosedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3445
        self.vars.append({"name": "hostInformations", "type": "CharacterMinimalInformations", "value": ""})
