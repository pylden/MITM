from module.protocol.network.message import Message


class JobCrafterDirectoryAddMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2605
        self.listEntry = {"type": "JobCrafterDirectoryListEntry", "value": ""}
