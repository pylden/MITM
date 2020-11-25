from module.protocol.network.message import Message


class TeleportToBuddyCloseMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6271
        self.dungeonId = {"type": "uint", "value": ""}
        self.buddyId = {"type": "Number", "value": ""}
