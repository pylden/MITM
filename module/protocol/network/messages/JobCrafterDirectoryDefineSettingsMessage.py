from module.protocol.network.message import Message


class JobCrafterDirectoryDefineSettingsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 832
        self.settings = {"type": "JobCrafterDirectorySettings", "value": ""}
