from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IdolPartyRefreshMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2232
        self.partyIdol = {"type": "PartyIdol", "value": ""}
