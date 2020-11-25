from module.protocol.network.message import Message


class IdolPartyRefreshMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2232
        self.partyIdol = {"type": "PartyIdol", "value": ""}
