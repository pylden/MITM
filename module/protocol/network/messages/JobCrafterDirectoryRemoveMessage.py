from module.protocol.network.message import Message


class JobCrafterDirectoryRemoveMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2166
        self.jobId = {"type": "uint", "value": ""}
        self.playerId = {"type": "Number", "value": ""}
