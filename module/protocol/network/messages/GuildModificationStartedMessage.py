from module.protocol.network.message import Message


class GuildModificationStartedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2536
        self.canChangeName = {"type": "Boolean", "value": ""}
        self.canChangeEmblem = {"type": "Boolean", "value": ""}
