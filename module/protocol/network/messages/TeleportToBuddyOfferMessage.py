from module.protocol.network.message import Message


class TeleportToBuddyOfferMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5460
        self.dungeonId = {"type": "uint", "value": ""}
        self.buddyId = {"type": "Number", "value": ""}
        self.timeLeft = {"type": "uint", "value": ""}
