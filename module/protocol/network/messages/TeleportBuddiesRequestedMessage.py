from module.protocol.network.message import Message


class TeleportBuddiesRequestedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9376
        self.dungeonId = {"type": "uint", "value": ""}
        self.inviterId = {"type": "Number", "value": ""}
        self.invalidBuddiesIds = {"type": "Vector.<Number>", "value": ""}
