from module.protocol.network.message import Message


class TeleportBuddiesMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 650
        self.dungeonId = {"type": "uint", "value": ""}
