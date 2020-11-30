from module.protocol.network.messages.NetworkMessage import NetworkMessage


class InviteInHavenBagOfferMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1021
        self.hostInformations = {"type": "CharacterMinimalInformations", "value": ""}
        self.timeLeftBeforeCancel = {"type": "int", "value": ""}
