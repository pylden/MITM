from module.protocol.network.message import Message


class GuildPaddockRemovedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6712
        self.paddockId = {"type": "Number", "value": ""}
