from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PartyInvitationRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1758
        self.vars.append({"name": "name", "type": "String", "value": ""})
