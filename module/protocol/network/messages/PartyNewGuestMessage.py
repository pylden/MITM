from module.protocol.network.message import Message


class PartyNewGuestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2749
        self.guest = {"type": "PartyGuestInformations", "value": ""}
