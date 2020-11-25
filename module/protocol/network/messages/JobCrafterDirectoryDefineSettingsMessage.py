from module.protocol.network.message import Message


class JobCrafterDirectoryDefineSettingsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 832
        self.settings = {"type": "JobCrafterDirectorySettings", "value": ""}
