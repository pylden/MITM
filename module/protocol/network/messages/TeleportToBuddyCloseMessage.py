from module.protocol.network.message import Message


class TeleportToBuddyCloseMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6271
        self.dungeonId = {"type": "uint", "value": ""}
        self.buddyId = {"type": "Number", "value": ""}
