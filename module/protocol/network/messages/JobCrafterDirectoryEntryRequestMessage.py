from module.protocol.network.message import Message


class JobCrafterDirectoryEntryRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2083
        self.playerId = {"type": "Number", "value": ""}
