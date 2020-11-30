from module.protocol.network.messages.PartyUpdateLightMessage import PartyUpdateLightMessage


class PartyEntityUpdateLightMessage(PartyUpdateLightMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        PartyUpdateLightMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8730
        self.indexId = {"type": "uint", "value": ""}
