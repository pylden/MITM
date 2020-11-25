from module.protocol.network.message import Message


class JobCrafterDirectoryListRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2533
        self.jobId = {"type": "uint", "value": ""}
