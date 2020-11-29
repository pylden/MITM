from module.protocol.network.messages.NetworkMessage import NetworkMessage


class InviteInHavenBagMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9753
        self.vars.append({"name": "guestInformations", "type": "CharacterMinimalInformations", "value": ""})
        self.vars.append({"name": "accept", "type": "Boolean", "value": ""})
