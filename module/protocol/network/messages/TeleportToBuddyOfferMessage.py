from module.protocol.network.message import Message


class TeleportToBuddyOfferMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5460
        self.dungeonId = {"type": "uint", "value": ""}
        self.buddyId = {"type": "Number", "value": ""}
        self.timeLeft = {"type": "uint", "value": ""}
