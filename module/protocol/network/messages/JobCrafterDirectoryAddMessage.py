from module.protocol.network.message import Message


class JobCrafterDirectoryAddMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2605
        self.listEntry = {"type": "JobCrafterDirectoryListEntry", "value": ""}
