from module.protocol.network.message import Message


class JobCrafterDirectoryEntryRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2083
        self.playerId = {"type": "Number", "value": ""}
