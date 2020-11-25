from module.protocol.network.message import Message


class PartyNewGuestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2749
        self.guest = {"type": "PartyGuestInformations", "value": ""}
