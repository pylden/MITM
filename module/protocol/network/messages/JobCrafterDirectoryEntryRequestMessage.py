from module.protocol.network.message import Message


class JobCrafterDirectoryEntryRequestMessage(Message):
    def __init__(self):
        self.id = 2083
