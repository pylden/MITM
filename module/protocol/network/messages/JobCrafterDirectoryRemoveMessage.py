from module.protocol.network.message import Message


class JobCrafterDirectoryRemoveMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2166
        self.jobId = {"type": "uint", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
