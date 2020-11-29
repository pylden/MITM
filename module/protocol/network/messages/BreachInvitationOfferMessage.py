from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BreachInvitationOfferMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5041
        self.vars.append({"name": "host", "type": "CharacterMinimalInformations", "value": ""})
        self.vars.append({"name": "timeLeftBeforeCancel", "type": "uint", "value": ""})
