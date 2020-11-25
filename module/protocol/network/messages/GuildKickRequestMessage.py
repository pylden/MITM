from module.protocol.network.message import Message


class GuildKickRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2484
        self.kickedId = {"type": "Number", "value": ""}
